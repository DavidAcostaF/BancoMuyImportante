from django.db import models
from apps.cuenta.models import Cuenta
# Create your models here.


class Transaccion(models.Model):
    TRANSFERENCIA = 'TR'
    SIN_CUENTA = 'SC'
    TIPOS_TRANSACCION = [
        (TRANSFERENCIA, 'Transferencia'),
        (SIN_CUENTA, 'Sin Cuenta'),
    ]
    
    fecha = models.DateTimeField(auto_now_add=True)
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    tipo = models.CharField(max_length=2, choices=TIPOS_TRANSACCION)
    cuenta = models.ForeignKey(Cuenta, on_delete=models.CASCADE)
    
    
    class Meta:
        abstract = True


class Transferencia(Transaccion):
    folio = models.CharField(max_length=50)

    def save(self, *args, **kwargs):
        self.tipo = self.TRANSFERENCIA
        super().save(*args, **kwargs)

class SinCuenta(Transaccion):
    contrasena = models.CharField(max_length=50)

    def save(self, *args, **kwargs):
        self.tipo = self.SIN_CUENTA
        super().save(*args, **kwargs)
    
