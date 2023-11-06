from django.shortcuts import render
from .models import Producto

def lista_productos(request):
    # Obtiene todos los productos de la base de datos
    productos = Producto.objects.all()
    
    # Pasa los productos a la plantilla HTML
    return render(request, 'productos/lista_productos.html', {'productos': productos})
