from django.db import models

# Create your models here.
class tipo_vehiculo(models.Model):
    idtipo = models.AutoField(primary_key=True)
    nombre_vehiculo = models.CharField(max_length=30)

    def __str__(self):
        return self.nombre_vehiculo

class Auto(models.Model):
    PatenteAuto = models.AutoField(primary_key=True)
    idtipo = models.ForeignKey(tipo_vehiculo, on_delete=models.CASCADE)
    marca = models.CharField(max_length=20)
    estado = models.CharField(max_length=20)
    modelo = models.CharField(max_length=50)
    color = models.CharField(max_length=20)
    anno = models.CharField(max_length=20)
    file = models.FileField(upload_to="img/autos")
    comentario = models.CharField(max_length=200)

    def __str__(self):
        return self.modelo


class Motocicleta(models.Model):
    PatenteMoto = models.AutoField(primary_key=True)
    idtipo = models.ForeignKey(tipo_vehiculo, on_delete=models.CASCADE)
    marca =  models.CharField(max_length=20)
    estado = models.CharField(max_length=20)
    modelo = models.CharField(max_length=50)
    color = models.CharField(max_length=20)
    anno = models.CharField(max_length=20)
    file = models.FileField(upload_to="img/motos")
    comentario = models.CharField(max_length=200)

    def __str__(self):
        return self.modelo 