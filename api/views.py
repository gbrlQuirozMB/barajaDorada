from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, DestroyAPIView, RetrieveUpdateAPIView
from rest_framework_swagger.views import get_swagger_view

from comercio.models import *
from .exceptions import *
from .serializers import *


schema_view = get_swagger_view(title='Baraja Dorada API')

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
    """
    sorteo -- id del sorteo a buscar
    """
    serializer_class = CartaSerializer

    def get_queryset(self):
        queryset = Carrito.objects.all()
        sorteo = self.request.query_params.get('sorteo', None)
        if sorteo is not None:
            # obtenemos los id de carta que cumplan con el token de sesion y con sorteo_id
            queryset = queryset.filter(sorteo=sorteo).values('carta')
            # obtenemos las cartas que no se han utilizado para ese sorteo
            queryset = Carta.objects.exclude(id__in=queryset)
        else:
            return None
        return queryset


# ----------------------------------------------------------------------------------Sorteo
class SorteoCreateView(CreateAPIView):
    serializer_class = SorteoSerializer

    def post(self, request, *args, **kwargs):
        serializer = SorteoSerializer(data=request.data)
        if serializer.is_valid():
            return self.create(request, *args, **kwargs)
        raise CamposIncorrectos(serializer.errors)


class SorteoListView(ListAPIView):
    """
    activo -- true/false para mostar sorteos vigentes
    """
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

    def post(self, request, *args, **kwargs):
        principal = self.request.data.get('principal')
        if principal:
            sorteo = self.request.data.get('sorteo')
            Imagen.objects.filter(sorteo=sorteo).update(principal=False)

        return self.create(request, *args, **kwargs)


class ImagenListView(ListAPIView):
    queryset = Imagen.objects.all()
    serializer_class = ImagenSerializer


class ImagenDetailView(RetrieveAPIView):
    queryset = Imagen.objects.filter()
    serializer_class = ImagenSerializer


class ImagenUpdateView(RetrieveUpdateAPIView):
    queryset = Imagen.objects.filter()
    serializer_class = ImagenSerializer

    def put(self, request, *args, **kwargs):
        principal = self.request.data.get('principal')
        if principal:
            pk = kwargs['pk']
            sorteo = Imagen.objects.filter(id=pk).values_list('sorteo', flat=True)
            Imagen.objects.filter(sorteo=sorteo[0]).update(principal=False)

        return self.update(request, *args, **kwargs)


class ImagenDeleteView(DestroyAPIView):
    queryset = Imagen.objects.filter()
    serializer_class = ImagenSerializer
