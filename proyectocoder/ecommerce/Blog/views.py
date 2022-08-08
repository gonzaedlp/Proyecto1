from django.shortcuts import render
from Blog.models import Articles

def create_article(request):
    new_article= Articles.objects.create(titulo='alimento saludable', descripcion='los alimentos saludables son...')
    context={
        'new_article':new_article
    }
    return render(request, 'Blog/crear_articulo.html', context=context)

def listar_articulos(request):
    listar_articulos= Articles.objects.all()
    context={
        'listar_articulos':listar_articulos
    }
    return render(request, 'Blog/listar_articulos.html', context=context)

def primer_formulario(request):
    return render(request, 'primer_formulario.html', context={})
