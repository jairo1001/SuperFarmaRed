from django.db import models
from products.models import Producto

class Carrito(models.Model):
    total_farmacias_economicas = models.DecimalField(max_digits=6, decimal_places=2, null=True)
    total_fybeca = models.DecimalField(max_digits=6, decimal_places=2, null=True)
    total_pharmacys = models.DecimalField(max_digits=6, decimal_places=2, null=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return "Cart id: {}".format(self.id)


class CarritoItem(models.Model):
    carrito = models.ForeignKey(Carrito, null=True, blank=True, on_delete=models.CASCADE)
    # Basket foriegn key
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.IntegerField(default=1)
    total_producto = models.DecimalField(max_digits=6, decimal_places=2, null=True)
    # product total
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        try:
            return str(self.carrito.id)
        except AttributeError:
            return self.producto.nombre
