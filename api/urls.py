from django.urls import path, re_path

from .views import *

app_name = 'api'

urlpatterns = [
    # ----------------------------------------------------------------------------------Carta
    path('cartas/create/', CartaCreateView.as_view(), ),
    path('cartas/list/', CartaListView.as_view(), ),
    path('cartas/detail/<pk>/', CartaDetailView.as_view(), ),
    path('cartas/update/<pk>/', CartaUpdateView.as_view(), ),
    path('cartas/delete/<pk>/', CartaDeleteView.as_view(), ),
    # ----------------------------------------------------------------------------------Sorteo
    path('sorteos/create/', SorteoCreateView.as_view(), ),
    path('sorteos/list/', SorteoListView.as_view(), ),
    path('sorteos/detail/<pk>/', SorteoDetailView.as_view(), ),
    path('sorteos/update/<pk>/', SorteoUpdateView.as_view(), ),
    path('sorteos/delete/<pk>/', SorteoDeleteView.as_view(), ),
]
