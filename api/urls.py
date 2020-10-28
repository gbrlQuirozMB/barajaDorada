from django.urls import path

from .views import *

app_name = 'api'

urlpatterns = [
    # ----------------------------------------------------------------------------------Carta
    path('cartas/create/', CartaCreateView.as_view(), ),
    path('cartas/list/', CartaListView.as_view(), ),
    path('cartas/detail/<pk>/', CartaDetailView.as_view(), ),
    path('cartas/update/<pk>/', CartaUpdateView.as_view(), ),
    path('cartas/delete/<pk>/', CartaDeleteView.as_view(), ),

]
