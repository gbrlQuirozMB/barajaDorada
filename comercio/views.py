from datetime import datetime

import stripe
from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render
from django.views.generic.base import TemplateView
from rest_framework import permissions
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.generics import ListAPIView, CreateAPIView

from api.exceptions import *
from .serializers import *


class CsrfExemptSessionAuthentication(SessionAuthentication):

    def enforce_csrf(self, request):
        return  # To not perform the csrf check previously happening


# ----------------------------------------------------------------------------------Carrito
class CarritoCreateView(CreateAPIView):
    """
    tokenCompra -- No requerido, se genera automaticamente para  guardar fecha y hora de la compra
    tokenStripe -- Requerido, aqui se pone el token que genera Stripe para hacer la compra
    """
    serializer_class = CarritoSerializer
    authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)

    def post(self, request, *args, **kwargs):

        serializer = CarritoSerializer(data=request.data)
        if not serializer.is_valid():
            raise CamposIncorrectos(serializer.errors)

        stripe.api_key = settings.STRIPE_API_KEY
        # ---saber fecha y hora de la compra
        myDate = datetime.now()
        tokenCompra = myDate.strftime('%d-%m-%Y-%H:%M:%S')
        request.data['tokenCompra'] = tokenCompra
        # ---checar si la carta ya se compro
        # sorteo = self.request.query_params.get('sorteo', None) # parametros en el url
        # carta = self.request.query_params.get('carta', None) # parametros en el url
        sorteo = self.request.data.get('sorteo')  # valores del json
        carta = self.request.data.get('carta')  # valores del json

        cuenta = Carrito.objects.filter(carta=carta, sorteo=sorteo).count()
        if cuenta > 0:
            raise ResponseError('La carta ya se compro', 409)
        # ---cobrar
        try:
            tokenStripe = request.data.get('tokenStripe')
            precio = Sorteo.objects.filter(id=sorteo).values_list('costoCarta', flat=True)
            stripe.Charge.create(
                amount=int(precio[0]) * 100,
                currency='MXN',
                description='Baraja Dorada',
                source=tokenStripe
            )
        except:
            raise ResponseError('Error con Stripe', 500)
        # ---mandar correo
        try:
            nl = '\n'
            nombre = self.request.data.get('nombreCompleto')
            email = self.request.data.get('email')
            nombreCarta = Carta.objects.filter(id=carta).values_list('nombre', flat=True)
            datosSorteo = Sorteo.objects.filter(id=sorteo).values_list('titulo', 'fechaHoraSorteo')
            text_content = f'Hola {nombre},{nl} Haz comprado la carta: {nombreCarta[0]},{nl} Para el sorteo: {datosSorteo[0][0]},{nl} A llevarse a cabo: {datosSorteo[0][1].strftime("%d-%b-%Y %H:%Mh")}'
            send_mail(
                'Compra Baraja Dorada',
                text_content,
                'contacto@lbd.mx',
                [email],
                fail_silently=False,
            )
        except:
            raise ResponseError('Error al enviar correo', 500)

        return self.create(request, *args, **kwargs)


class CompradoresListView(ListAPIView):
    """
    sorteo=id -- id del sorteo a buscar
    """
    serializer_class = CarritoSerializer
    permission_classes = (permissions.AllowAny,)

    def get_queryset(self):
        queryset = Carrito.objects.all()
        sorteo = self.request.query_params.get('sorteo', None)
        if sorteo is not None:
            queryset = queryset.filter(sorteo=sorteo)
        else:
            return None
        return queryset


class DummyPagosView(TemplateView):
    template_name = 'comercio/dummy-pagos.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['key'] = 'pk_test_TOPh5XSzYRTUMTsYGSD5js3G00CJodwZ02'
        return context


def token(request):
    if request.method == 'POST':
        stripe.api_key = settings.STRIPE_API_KEY
        # stripe.Charge.create(
        #     amount=369 * 100,
        #     currency='MXN',
        #     description='Baraja Dorada',
        #     source=request.POST['stripeToken']
        # )
        # return render(request, 'comercio/token.html')
        stripeToken = request.POST['stripeToken']
        print(stripeToken)
        return render(request, 'comercio/token.html', context={'stripeToken': stripeToken}, )
