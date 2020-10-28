from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, DestroyAPIView, RetrieveUpdateAPIView

from .serializers import *


# ----------------------------------------------------------------------------------Carta
class CartaCreateView(CreateAPIView):
    serializer_class = CartaSerializer


class CartaListView(ListAPIView):
    queryset = Carta.objects.all()
    serializer_class = CartaSerializer


class CartaDetailView(RetrieveAPIView):
    queryset = Carta.objects.filter()
    serializer_class = CartaSerializer


class CartaUpdateView(RetrieveUpdateAPIView):
    queryset = Carta.objects.filter()
    serializer_class = CartaSerializer


class CartaDeleteView(DestroyAPIView):
    queryset = Carta.objects.filter()
    serializer_class = CartaSerializer



