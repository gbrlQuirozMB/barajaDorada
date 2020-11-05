
from django.urls import path

from . import views
from .views import *

app_name = 'comercio'

urlpatterns = [
    # ----------------------------------------------------------------------------------Carta
    path('comprar-carta/', CarritoCreateView.as_view(), ),
    path('mostrar-carrito/', CarritoListView.as_view(), ),
    path('quitar-carta/<pk>/', CarritoDeleteView.as_view(), ),
    path('finalizar-compra/', ComprarView.as_view(), ),

    path('session/', CrearSession.as_view(), ),
    path('intento/', CrearIntento.as_view(), ),
    path('datos-tarjeta/', views.index, ),

    # path('cartas/list/', CartaListView.as_view(), ),
    # path('cartas/detail/<pk>/', CartaDetailView.as_view(), ),
    # path('cartas/update/<pk>/', CartaUpdateView.as_view(), ),
    # path('cartas/delete/<pk>/', CartaDeleteView.as_view(), ),

]
