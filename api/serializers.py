from rest_framework import serializers

from .models import *


class CartaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Carta
        fields = '__all__'

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['imagen'] = instance.imagen.url
        return representation


class SorteoSerializer(serializers.ModelSerializer):
    imagen = serializers.SerializerMethodField()

    def get_imagen(self, obj):
        querysetI = Imagen.objects.filter(sorteo=obj.id, principal=True).values('imagen')[:1]
        dato = None
        for datos in querysetI:
            dato = '/uploads/' + datos['imagen']
        return dato

    class Meta:
        model = Sorteo
        fields = ['id', 'titulo', 'descripcion', 'detalles', 'activo', 'fechaHoraSorteo', 'imagen']


class ImagenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Imagen
        fields = '__all__'

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['imagen'] = ''
        if instance.imagen.url is not None:
            representation['imagen'] = instance.imagen.url
        return representation


class SorteoDetailSerializer(serializers.ModelSerializer):
    imagenes = ImagenSerializer(required=False, many=True)
    fechaHoraSorteo = serializers.DateTimeField(format='%d-%b-%Y %H:%Mh')

    class Meta:
        model = Sorteo
        fields = ['id', 'titulo', 'descripcion', 'detalles', 'activo', 'fechaHoraSorteo', 'imagenes']
