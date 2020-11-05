from rest_framework import serializers

from api.serializers import CartaSerializer
from .models import *


class CarritoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Carrito
        fields = '__all__'


class CarritoListSerializer(serializers.ModelSerializer):
    carta = CartaSerializer(required=False)
    costoCarta = serializers.SerializerMethodField()

    def get_costoCarta(self, obj):
        precio = Sorteo.objects.filter(id=obj.sorteo_id).values_list('costoCarta', flat=True)
        return precio[0]

    class Meta:
        model = Carrito
        fields = ['id', 'costoCarta', 'carta']
