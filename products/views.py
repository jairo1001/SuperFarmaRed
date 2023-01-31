from django.shortcuts import render, get_object_or_404
from .models import Producto, Categoria
from . import cargar_precios as cp

#filtrado de productos por categoria
def filtered_products(request, category_slug):
    categories = Categoria.objects.all()
    products = Producto.objects.all()
    if category_slug:
        category = get_object_or_404(Categoria, slug=category_slug)
        products = products.filter(categoria=category)
    print(category, products)
    template = "products/categories/filter.html"
    context = {"categories": categories, "product_query_set": products, "category": category}
    return render(request, template, context)

#definicion del metodo para productos
def main_products(request):
    #obtener el listado de productos
    products = Producto.objects.all()
    return render(request, "products/main_products.html", {"products": products})

#definicion del metodo para categorias
def categories(request):
    categories = Categoria.objects.all()
    return render(request, "products/categories.html", {"categories": categories})

def actualizacion_precios(request):
    products = cp.lista_productos_eliminados()
    return render(request,"products/sincronizado.html",{"products": products})