import random
from datetime import datetime

import stripe
from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.generics import ListAPIView, CreateAPIView, DestroyAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from django.core.mail import EmailMultiAlternatives


from .serializers import *


# pk_test_TOPh5XSzYRTUMTsYGSD5js3G00CJodwZ02

# ----------------------------------------------------------------------------------Carrito
class CarritoCreateView(CreateAPIView):
    serializer_class = CarritoSerializer

    def post(self, request, *args, **kwargs):
        if request.data.get('token') is None:
            myDate = datetime.now()
            token = myDate.strftime('%d-%m-%Y-%H:%M:%S-') + str(random.randint(10000, 99999))
            request.data['token'] = token
            return self.create(request, *args, **kwargs)
        return self.create(request, *args, **kwargs)


class CarritoListView(ListAPIView):
    serializer_class = CarritoListSerializer

    def get_queryset(self):
        queryset = Carrito.objects.all()
        token = self.request.query_params.get('token', None)
        sorteo = self.request.query_params.get('sorteo', None)
        if token is not None and sorteo is not None:
            queryset = queryset.filter(token=token, sorteo=sorteo)
        else:
            return None
        return queryset


class CarritoDeleteView(DestroyAPIView):
    queryset = Carrito.objects.filter()
    serializer_class = CarritoSerializer


class ComprarView(APIView):
    def post(self, request, *args, **kwargs):
        response = {}
        stripe.api_key = 'sk_test_rr9VKE4Po9YQip41vMw9x18y000h9ssG70'
        try:
            tokenStripe = request.data.get('token')
            tokenCarrito = request.data.get('tokenCarrito')
            cuenta = Carrito.objects.filter(token=tokenCarrito).count()
            sorteo = Carrito.objects.filter(token=tokenCarrito).values('sorteo')[:1]
            precio = Sorteo.objects.filter(id=sorteo).values_list('costoBoleto', flat=True)
            total = cuenta * precio[0]

            # stripe.Charge.create(
            #     amount=int(total) * 100,
            #     currency='MXN',
            #     description='Baraja Dorada',
            #     source=tokenStripe
            # )

            # text_content = """
            #     Hola Gabriel,
            #     haz comprado a baraja dorada
            # """
            # email = EmailMultiAlternatives("Baraja Dorada", text_content, "no-reply@fierrosylaminas.com", ['gabriel@mb.company'])
            # email.send()

            response['code'] = 200
            response['message'] = f'Cobro exitoso: {total}'
        except:
            response['code'] = 500
            response['message'] = 'Algo fallo en Stripe'
        return Response(response, status=response['code'])


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
