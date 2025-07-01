from django.db import models

# Create your models here.
class Categoria(models.Model):
    nombre = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.nombre

class ProductUnits(models.TextChoices):
    UNITS = 'u', 'unidades'
    KG = 'kg', 'kilogramos'

class Producto(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    unidades = models.CharField(
        max_length=2,
        choices=ProductUnits.choices,
        default=ProductUnits.UNITS
    )
    disponible = models.BooleanField(blank=True, default=True)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.nombre} ({self.categoria.nombre})"