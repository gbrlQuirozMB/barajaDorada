
from django.urls import path

from . import views
from .views import *
from django.views.decorators.csrf import csrf_exempt

app_name = 'comercio'

urlpatterns = [
    # ----------------------------------------------------------------------------------Carta
    path('comprar-carta/', csrf_exempt(CarritoCreateView.as_view()), ),
    path('compradores/', CompradoresListView.as_view(), ),

    # ----------------------------------------------------------------------------------stripe local NO FUNCIONA!!!
    # path('session/', CrearSession.as_view(), ),
    # path('intento/', CrearIntento.as_view(), ),
    # path('datos-tarjeta/', views.index, ),


]
