from datetime import datetime

import stripe
from django.conf import settings
from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.generics import ListAPIView, CreateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import *


# ----------------------------------------------------------------------------------Carrito
class CarritoCreateView(CreateAPIView):
    serializer_class = CarritoSerializer

    def post(self, request, *args, **kwargs):
        stripe.api_key = settings.STRIPE_API_KEY
        response = {}
        # ---saber fecha y hora de la compra
        myDate = datetime.now()
        tokenCompra = myDate.strftime('%d-%m-%Y-%H:%M:%S')
        request.data['tokenCompra'] = tokenCompra
        # ---checar si la carta ya se compro
        # sorteo = self.request.query_params.get('sorteo', None) # parametros en el url
        # carta = self.request.query_params.get('carta', None) # parametros en el url
        sorteo = self.request.data.get('sorteo')  # valores del json
        carta = self.request.data.get('carta')  # valores del json

        if carta is not None and sorteo is not None:
            cuenta = Carrito.objects.filter(carta=carta, sorteo=sorteo).count()
            if cuenta > 0:
                response['code'] = 409
                response['message'] = 'La carta ya se compro'
                return Response(response, status=response['code'])
            # ---cobrar
            try:
                tokenStripe = request.data.get('tokenStripe')
                precio = Sorteo.objects.filter(id=sorteo).values_list('costoCarta', flat=True)
                # stripe.Charge.create(
                #     amount=int(precio[0]) * 100,
                #     currency='MXN',
                #     description='Baraja Dorada',
                #     source=tokenStripe
                # )
            except:
                response['code'] = 500
                response['message'] = 'Error con Stripe'
                return Response(response, status=response['code'])
            # ---mandar correo
            try:
                nl = '\n'
                nombre = self.request.data.get('nombreCompleto')
                email = self.request.data.get('email')
                nombreCarta = Carta.objects.filter(id=carta).values_list('nombre', flat=True)
                datosSorteo = Sorteo.objects.filter(id=sorteo).values_list('titulo', 'fechaHoraSorteo')
                text_content = f'Hola {nombre},{nl} Haz comprado la carta: {nombreCarta[0]},{nl} Para el sorteo: {datosSorteo[0][0]},{nl} A llevarse a cabo: {datosSorteo[0][1].strftime("%d-%b-%Y %H:%Mh")}'
                # send_mail(
                #     'Compra Baraja Dorada',
                #     text_content,
                #     'contacto@lbd.mx',
                #     [email],
                #     fail_silently=False,
                # )
            except:
                response['code'] = 500
                response['message'] = 'Error al enviar correo'
                return Response(response, status=response['code'])

        else:
            response['code'] = 400
            response['message'] = 'Datos incorrectos'
            return Response(response, status=response['code'])

        return self.create(request, *args, **kwargs)


class CompradoresListView(ListAPIView):
    serializer_class = CarritoSerializer

    def get_queryset(self):
        queryset = Carrito.objects.all()
        sorteo = self.request.query_params.get('sorteo', None)
        if sorteo is not None:
            queryset = queryset.filter(sorteo=sorteo)
        else:
            return None
        return queryset


class CrearSession(APIView):
    def post(self, request, *args, **kwargs):
        stripe.api_key = 'sk_test_rr9VKE4Po9YQip41vMw9x18y000h9ssG70'
        session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[{
                'price_data': {
                    'currency': 'MXN',
                    'product_data': {
                        'name': 'T-shirt',
                    },
                    'unit_amount': 369 * 100,
                },
                'quantity': 1,
            }],
            mode='payment',
            success_url='https://example.com/success',
            cancel_url='https://example.com/cancel',
        )
        response = {
            'id': session.id
        }
        return JsonResponse(response, status=200)


class CrearIntento(APIView):
    def get(self, request, *args, **kwargs):
        stripe.api_key = 'sk_test_rr9VKE4Po9YQip41vMw9x18y000h9ssG70'
        intent = stripe.PaymentIntent.create(
            amount=369 * 100,
            currency='MXN',
            payment_method_types=['card'],
        )
        print(intent.client_secret)
        response = {
            "client_secret": intent.client_secret
        }
        return JsonResponse(response, status=200)


def index(request):
    # return render(request,'comercio/index.html')
    stripe.api_key = 'sk_test_rr9VKE4Po9YQip41vMw9x18y000h9ssG70'
    intent = stripe.PaymentIntent.create(
        amount=369 * 100,
        currency='MXN',
        payment_method_types=['card'],
    )
    return render(request, 'comercio/prueba.html', context={'client_secret': intent.client_secret}, )
