from django.http import HttpResponse
from django.shortcuts import render
from .models import Categoria

def index(request):
    return HttpResponse("Hello mundo.")
# Create your views here.
def contact(request, name):
    return HttpResponse(f"Bienvenido {name} a la clase.")


def categorias(request):
    filtro_nombre = request.GET.get("nombre", "")
    if filtro_nombre:
        categorias = Categoria.objects.filter(nombre=filtro_nombre)
    else:
        categorias = Categoria.objects.all()
    return render(request, "categorias.html",
                   {"categorias": categorias, "filtro_nombre": filtro_nombre})