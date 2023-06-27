from django.contrib import admin
from .models import  tipo_vehiculo, Auto, Motocicleta
# Register your models here.

admin.site.register(tipo_vehiculo)
admin.site.register(Auto)
admin.site.register(Motocicleta)