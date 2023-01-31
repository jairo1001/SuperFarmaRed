import re
import requests
from bs4 import BeautifulSoup
from products.models import Producto
#eliminar un producto de la base de datos
def eliminar_producto(url):
    if "medicity-farmacias" in url:
        producto = Producto.objects.get(url_farmacias_economicas=url)
        producto.delete()
    elif "www.fybeca.com" in url:
        producto = Producto.objects.get(url_fybeca = url)
        producto.delete()      
    elif "pharmacys-market" in url:
        producto = Producto.objects.get(url_pharmacys = url)
        producto.delete()
        

#extraer precio de farmacias economicas
def extraer_precio_farmacias_economicas(url):
    r=requests.get(url)
    soup = BeautifulSoup(r.text, 'lxml')
    test=soup.find('span', class_="sc-ifAKCX hADVmt")
    precio=test.getText()
    precio = [float(s) for s in re.findall(r'-?\d+\.?\d*', precio)]
    precio = precio[0]
    return precio
                
#extraer precio de fybeca
def extraer_precio_fybeca(url):
    r=requests.get(url)
    soup = BeautifulSoup(r.text, 'lxml')
    precio=soup.find('div',class_="large-price d-flex")
    precio=precio.span
    precio=precio.getText()
    precio = [float(s) for s in re.findall(r'-?\d+\.?\d*', precio)]
    precio = precio[0]
    return precio

#extraer precios de pharmacys
def extraer_precio_pharmacys(url):
    r=requests.get(url)
    soup = BeautifulSoup(r.text, 'lxml')
    test=soup.find('span', class_="sc-ifAKCX hADVmt")
    precio=test.getText()
    precio = [float(s) for s in re.findall(r'-?\d+\.?\d*', precio)]
    precio = precio[0]
    return precio


