from django.contrib import admin
from .models import Categoria,Producto

#administracion de Categorias para el superusuario
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ['nombre','slug','imagen']
    prepopulated_fields = {'slug':('nombre',)}
    list_editable = ['imagen']

admin.site.register(Categoria,CategoriaAdmin)

#administracion de Productos para el superusuario
class ProductoAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('nombre',)}
    list_display = ['nombre', 'slug' , 'categoria' , 'imagen' , 'compuesto']
    list_filter = ['categoria','fecha_creacion']
    list_editable = ['imagen']

admin.site.register(Producto,ProductoAdmin)



