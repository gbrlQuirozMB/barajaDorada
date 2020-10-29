from rest_framework import serializers

from .models import *


class CartaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Carta
        fields = '__all__'


class SorteoSerializer(serializers.ModelSerializer):
    imagen = serializers.SerializerMethodField()

    def get_imagen(self, obj):
        querysetI = Imagen.objects.filter(sorteo=obj.id, principal=True).values('imagen')[:1]
        dato = None
        for datos in querysetI:
            dato = datos['imagen']
        return dato

    class Meta:
        model = Sorteo
        fields = ['id', 'titulo', 'descripcion', 'detalles', 'activo', 'fechaHoraSorteo', 'imagen']


class ImagenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Imagen
        fields = '__all__'


class SorteoDetailSerializer(serializers.ModelSerializer):
    imagenes = ImagenSerializer(required=False, many=True)

    class Meta:
        model = Sorteo
        fields = ['id', 'titulo', 'descripcion', 'detalles', 'activo', 'fechaHoraSorteo', 'imagenes']
