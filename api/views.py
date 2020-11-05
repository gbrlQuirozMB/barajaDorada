from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, DestroyAPIView, RetrieveUpdateAPIView

from comercio.models import *
from .serializers import *


# ----------------------------------------------------------------------------------Carta
# class CartaCreateView(CreateAPIView):
#     serializer_class = CartaSerializer


class CartaListView(ListAPIView):
    queryset = Carta.objects.all()
    serializer_class = CartaSerializer


class CartaDetailView(RetrieveAPIView):
    queryset = Carta.objects.filter()
    serializer_class = CartaSerializer


class CartaUpdateView(RetrieveUpdateAPIView):
    queryset = Carta.objects.filter()
    serializer_class = CartaSerializer


# class CartaDeleteView(DestroyAPIView):
#     queryset = Carta.objects.filter()
#     serializer_class = CartaSerializer


class CartasDisponiblesListView(ListAPIView):
    serializer_class = CartaSerializer

    def get_queryset(self):
        queryset = Carrito.objects.all()
        token = self.request.query_params.get('token', None)
        sorteo = self.request.query_params.get('sorteo', None)
        if token is not None and sorteo is not None:
            # obtenemos los id de carta que cumplan con el token de sesion y con sorteo_id
            queryset = queryset.filter(token=token, sorteo=sorteo).values('carta')
            # obtenemos las cartas que no se han utilizado para ese sorteo
            queryset = Carta.objects.exclude(id__in=queryset)
        else:
            return None
        return queryset


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
    serializer_class = SorteoDetailSerializer


class SorteoUpdateView(RetrieveUpdateAPIView):
    queryset = Sorteo.objects.filter()
    serializer_class = SorteoSerializer


class SorteoDeleteView(DestroyAPIView):
    queryset = Sorteo.objects.filter()
    serializer_class = SorteoSerializer


# ----------------------------------------------------------------------------------Imagen
class ImagenCreateView(CreateAPIView):
    serializer_class = ImagenSerializer


class ImagenListView(ListAPIView):
    queryset = Imagen.objects.all()
    serializer_class = ImagenSerializer


class ImagenDetailView(RetrieveAPIView):
    queryset = Imagen.objects.filter()
    serializer_class = ImagenSerializer


class ImagenUpdateView(RetrieveUpdateAPIView):
    queryset = Imagen.objects.filter()
    serializer_class = ImagenSerializer


class ImagenDeleteView(DestroyAPIView):
    queryset = Imagen.objects.filter()
    serializer_class = ImagenSerializer
