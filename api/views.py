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


# ----------------------------------------------------------------------------------Sorteo
class SorteoCreateView(CreateAPIView):
    serializer_class = SorteoSerializer


class SorteoListView(ListAPIView):
    serializer_class = SorteoSerializer

    def get_queryset(self):
        queryset = Sorteo.objects.all()
        activo = self.request.query_params.get('activo', None)
        if activo is not None:
            if activo == 'true':
                activo = True
            else:
                activo = False
            queryset = queryset.filter(activo=activo)
        return queryset


class SorteoDetailView(RetrieveAPIView):
    queryset = Sorteo.objects.filter()
    serializer_class = SorteoSerializer


class SorteoUpdateView(RetrieveUpdateAPIView):
    queryset = Sorteo.objects.filter()
    serializer_class = SorteoSerializer


class SorteoDeleteView(DestroyAPIView):
    queryset = Sorteo.objects.filter()
    serializer_class = SorteoSerializer
