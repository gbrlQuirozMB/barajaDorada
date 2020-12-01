from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from .views import *

app_name = 'comercio'

urlpatterns = [
    # ----------------------------------------------------------------------------------Carta
    path('comprar-carta/', csrf_exempt(CarritoCreateView.as_view()), ),
    path('compradores/', CompradoresListView.as_view(), ),

    # ----------------------------------------------------------------------------------stripe local!!!
    path('dummy-pagos/', DummyPagosView.as_view(), ),
    # path('dummy-pagos/', TemplateView.as_view(template_name='comercio/dummy-pagos.html'), ),
    path('token/', token, name='token'),
]
