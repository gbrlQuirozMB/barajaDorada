from api.models import *


# Create your models here.

class Carrito(models.Model):
    token = models.CharField(max_length=100, blank=True, null=True)
    carta = ForeignKey(Carta, on_delete=CASCADE, related_name='carritoCartas')
    sorteo = ForeignKey(Sorteo, on_delete=CASCADE, related_name='carritoSorteos')

    class Meta:
        db_table = 'carrito'
