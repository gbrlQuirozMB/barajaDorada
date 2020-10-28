from django.contrib import admin

# Register your models here.

from .models import Carta, Sorteo, Imagen

admin.site.register(Carta)
admin.site.register(Sorteo)
admin.site.register(Imagen)