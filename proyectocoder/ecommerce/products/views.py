from django.shortcuts import render
from products.models import Products

def create_products(request):
    new_product= Products.objects.create(name='pizza', price=20)
    context={
        'new_product':new_product
    }
    return render(request, 'products/crear_producto.html', context=context)

def listar_productos(request):
    listar_productos= Products.objects.all()
    context={
        'listar_productos':listar_productos
    }
    return render(request, 'products/listar_productos.html', context=context)

def primer_formulario(request):
    return render(request, 'primer_formulario.html', context={})
