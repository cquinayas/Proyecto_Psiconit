from django.db import models
from datetime import datetime

# Create your models here.
"""
class FormFactura(models.Model):
	numero = models.CharField(max_length=30, null=False, unique=True, verbose_name="Número")
	importe = models.DecimalField(max_digits=10, decimal_places=2, null=False, verbose_name="Importe")
	fecha = models.DateTimeField(default=datetime.now, null=True, blank=True, verbose_name="Fecha")
	cliente = models.CharField(max_length=200, null=False, verbose_name="Cliente")
	observacion = models.TextField(null=True, blank=True, verbose_name="Observación")
"""

class usuario(models.Model):
    username = models.CharField(max_length= 50, verbose_name="username")
    email = models.EmailField(max_length = 50,null=True, blank=True, verbose_name="email")
    first_name = models.CharField(max_length=50,null=True, blank=True,verbose_name="First name")
    last_name = models.CharField(max_length=50,null=True, blank=True,verbose_name="Last name")
    fecha = models.DateField(max_length=50, default=datetime.now, null=True, blank=True,verbose_name="Fecha de nacimiento")
    password1 = models.CharField(max_length= 50, null=True, blank=True)
    password2 = models.CharField(max_length= 50, null=True, blank=True)

def __str__(self):
    return self.username