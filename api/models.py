from django.db import models

# Create your models here.
from django.db.models import ForeignKey, CASCADE


class Cartas(models.Model):
    nombre = models.CharField(max_length=100)
    imagen = models.ImageField(upload_to='static/img/')

    class Meta:
        db_table = 'cartas'


class Sorteos(models.Model):
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    detalles = models.TextField(blank=True, null=True)
    activo = models.BooleanField(default=True)
    fechaHoraSorteo = models.DateTimeField(db_column='fecha_hora_sorteo')

    class Meta:
        db_table = 'sorteos'


class Imagenes(models.Model):
    imagen = models.ImageField(upload_to='static/img/')
    principal = models.BooleanField(default=False)
    sorteo = ForeignKey(Sorteos, on_delete=CASCADE, related_name='imagenes')

    class Meta:
        db_table = 'imagenes'
