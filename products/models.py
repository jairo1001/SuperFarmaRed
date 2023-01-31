from django.db import models
from django.urls import reverse

class Categoria(models.Model):
    nombre = models.CharField(max_length=150, db_index=True)
    slug = models.SlugField(max_length=50, unique=True, db_index=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)
    imagen = models.ImageField(default='imagen_por_defecto.png', blank=True)

    class Meta:
        ordering = ('nombre', )
        verbose_name = 'categoria'
        verbose_name_plural = 'categorias'

    def get_absolute_url(self):
        return reverse('products:filtered_products', args=[self.slug])

    def __str__(self):
        return self.nombre


class Producto(models.Model):
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=50, db_index=True)
    compuesto = models.CharField(max_length=100, db_index=True)

    url_farmacias_economicas = models.CharField(max_length=400, db_index=True)
    url_fybeca = models.CharField(max_length=400, db_index=True)
    url_pharmacys = models.CharField(max_length=400, db_index=True)

    precio_farmacias_economicas = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    precio_fybeca = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    precio_pharmacys = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)

    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)
    imagen = models.ImageField(default='imagen_por_defecto.png', blank=True)
    # make all thumbnails at most 140x140pixels

    class Meta:
        ordering = ('nombre', )
        index_together = (('id', 'slug'),)

    def __str__(self):
        return self.nombre
