from django.db import models

# Create your models here.

class Categoria(models.Model):
    nombre = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.nombre
class Producto(models.Model):
    categoria= models.ForeignKey(Categoria, on_delete=models.CASCADE)
    nombre= models.CharField(max_length=200)
    precio=models.DecimalField(max_digits=6, decimal_places=2)
    stock=models.IntegerField(default=0)
    pub_date=models.DateField('date published')
    def __str__(self):
        return self.nombre


class Cliente(models.Model):
    nombre=models.CharField(max_length=200)
    apellido=models.CharField(max_length=200)
    dni=models.CharField(blank=True, null=True,max_length=13 , default="--------")
    telef=models.CharField(blank=True, null=True,max_length=13, default="-----------")
    direccion=models.CharField(max_length=200)
    email=models.EmailField()
    fecha_naci=models.DateField('fecha de nacimiento')
    fecha_publi=models.DateTimeField('fecha de publicación')
    def __str__(self):
        return self.nombre