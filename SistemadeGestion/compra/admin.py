from django.contrib import admin
from .models import Producto, Proveedor
# Register your models here.

class ProveedorAdmin (admin.ModelAdmin):
    list_display = ['nombre','apellido','dni','provincia']
    search_fields = ['nombre','apellido','provincia']

class ProductoAdmin (admin.ModelAdmin):
    list_display = ['nombre','precio','categoria','stockactual','proveedor']
    search_fields = ['nombre','precio','categoria','stockactual','proveedor']

admin.site.register(Producto)
admin.site.register(Proveedor)