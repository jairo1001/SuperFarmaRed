from django.shortcuts import render, HttpResponseRedirect
from products.models import Producto
from .models import Carrito, CarritoItem

def basket_view(request):
    try:
        session_id = request.session["basket_id"]
    except KeyError:
        session_id = None

    if session_id:
        basket = Carrito.objects.get(id=session_id)
        context = {"basket": basket}
    else:
        empty_message = "Tu carrito está vacío"
        context = {"empty": True, "empty_message": empty_message}

    template = "basket/basket-view.html"
    return render(request, template, context)


def update_basket(request, slug):
    request.session.set_expiry(1800)
    try:
        quantity = request.GET.get("quantity")
        update_quantity = True
    except ValueError:
        quantity = None
        update_quantity = False

    try:
        session_id = request.session["basket_id"]
    except KeyError:
        new_basket = Carrito()
        new_basket.save()
        request.session["basket_id"] = new_basket.id
        session_id = new_basket.id

    basket = Carrito.objects.get(id=session_id)

    try:
        product = Producto.objects.get(slug=slug)
    except Producto.DoesNotExist:
        pass

    basket_item, created = CarritoItem.objects.get_or_create(carrito=basket, producto=product)


    if quantity and update_quantity:
        if int(quantity) <= 0:
            basket_item.delete()
        else:
            basket_item.cantidad = quantity
            basket_item.save()
    else:
        pass

    start_total_farmacias_economicas = 0.00
    start_total_fybeca = 0.00
    start_total_pharmacys = 0.00

    for item in basket.carritoitem_set.all():
        product_total_farmacias_economicas = float(item.producto.precio_farmacias_economicas) * item.cantidad
        product_total_fybeca = float(item.producto.precio_fybeca) * item.cantidad
        product_total_pharmacys = float(item.producto.precio_pharmacys) * item.cantidad
        start_total_farmacias_economicas += product_total_farmacias_economicas
        start_total_fybeca += product_total_fybeca
        start_total_pharmacys += product_total_pharmacys

    request.session["items_total"] = basket.carritoitem_set.count()

    basket.total_farmacias_economicas = start_total_farmacias_economicas
    basket.total_fybeca = start_total_fybeca
    basket.total_pharmacys = start_total_pharmacys

    basket.save()
    return HttpResponseRedirect(request.META.get("HTTP_REFERER"))
