
from django.urls import path

from . import views
from .views import *

app_name = 'comercio'

urlpatterns = [
    # ----------------------------------------------------------------------------------Carta
    path('comprar-carta/', CarritoCreateView.as_view(), ),
    path('compradores/', CompradoresListView.as_view(), ),

    # ----------------------------------------------------------------------------------stripe local NO FUNCIONA!!!
    path('session/', CrearSession.as_view(), ),
    path('intento/', CrearIntento.as_view(), ),
    path('datos-tarjeta/', views.index, ),


]
