from rest_framework import serializers

from .models import *


class CartaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Carta
        fields = '__all__'


class SorteoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sorteo
        fields = '__all__'


class ImagenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Imagen
        fields = '__all__si'
