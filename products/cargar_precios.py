from scripts import webscrapers as wb
from products.models import Producto
def lista_productos_eliminados():
    lista_eliminados=[]
    lista = Producto.objects.values_list('url_farmacias_economicas', 'url_fybeca' ,'url_pharmacys')
    lista_urls= list(lista)
    for rows in lista_urls:
        for url in rows:
            print(url)
            if "medicity-farmacias" in url:
                #comprobamos si existe el producto
                comprobacion=Producto.objects.filter(url_farmacias_economicas = url )
                comprobacion= list(comprobacion)
                if comprobacion:
                    try:
                        precio_farmacias_economicas = wb.extraer_precio_farmacias_economicas(url)
                        print(precio_farmacias_economicas)
                        producto = Producto.objects.get(url_farmacias_economicas = url )
                        producto.precio_farmacias_economicas = precio_farmacias_economicas
                        producto.save()
                    except AttributeError:
                        #sino encuentra el producto se lo elimina de la base de datos
                        producto = Producto.objects.get(url_farmacias_economicas = url )
                        lista_eliminados.append(producto)
                        wb.eliminar_producto(url)     

            elif "www.fybeca.com" in url:
                comprobacion=Producto.objects.filter(url_fybeca = url )
                comprobacion= list(comprobacion)
                if comprobacion:
                    try:
                        precio_fybeca = wb.extraer_precio_fybeca(url)
                        print(precio_fybeca)
                        producto = Producto.objects.get(url_fybeca = url)
                        producto.precio_fybeca = precio_fybeca
                        producto.save()
                    except IndexError:
                        #sino encuentra el producto se lo elimina de la base de datos
                        producto = Producto.objects.get(url_fybeca = url)
                        lista_eliminados.append(producto)
                        wb.eliminar_producto(url)  
                    except AttributeError:
                        #sino encuentra el producto se lo elimina de la base de datos
                        producto = Producto.objects.get(url_fybeca = url)
                        lista_eliminados.append(producto)
                        wb.eliminar_producto(url)        
            elif "pharmacys-market" in url:
                comprobacion=Producto.objects.filter(url_pharmacys = url )
                comprobacion= list(comprobacion)
                if comprobacion:
                    try:    
                        precio_pharmacys = wb.extraer_precio_pharmacys(url)
                        print(precio_pharmacys)
                        producto = Producto.objects.get(url_pharmacys=url)
                        producto.precio_pharmacys=precio_pharmacys
                        producto.save()
                    except AttributeError:
                        producto = Producto.objects.get(url_pharmacys=url)
                        lista_eliminados.append(producto)
                        wb.eliminar_producto(url)
            else:
                print("FLAG: El siguiente url es correcto? {}".format(url))
    return lista_eliminados
