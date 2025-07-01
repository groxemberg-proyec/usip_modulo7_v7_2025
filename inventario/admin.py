from django.contrib import admin
from .models import Categoria, Producto

admin.site.register(Categoria)

class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'categoria', 'precio', 'unidades', 'disponible')
    search_fields = ('nombre', 'categoria__nb.ombre')
    list_filter = ('disponible',)
    ordering = ('nombre',)

admin.site.register(Producto, ProductoAdmin)

# Register your models here.
