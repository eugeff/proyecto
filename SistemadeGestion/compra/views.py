from django.shortcuts import render, redirect, get_list_or_404, get_object_or_404
from .models import Producto, Proveedor
from django.http import HttpResponse,Http404
from django.views import generic
from django.forms import ModelForm
# Create your views here.

def index(request):
   numProd=Producto.objects.all().count()
   numProv=Proveedor.objects.all().count()
   numProdEle=Producto.objects.filter(categoria__exact='electronica').count()
   numProdElectrodom=Producto.objects.filter(categoria__exact='electrodomestico').count()
   numProdHo=Producto.objects.filter(categoria__exact='hogar').count()
   numProdDe=Producto.objects.filter(categoria__exact='deporte').count()
   return render(
        request,
        'compra/index.html',
        context={'numProd':numProd,'numProv':numProv,'numProdEle':numProdEle,'numProdElectrodom':numProdElectrodom,'numProdHo':numProdHo,'numProdDe':numProdDe},)



#Muestra todos los productos 
class mostrarProd(generic.ListView):
   model = Producto
   paginate_by = 10


# Formulario para registrar producto
def registrarProd(request):
    if request.method == 'POST':
      nombre = request.POST.get('nombre')
      precio = request.POST.get('precio')
      categoria = request.POST.get('categoria')
      stockactual = request.POST.get('stockactual')
      proveedor  = request.POST.get('proveedor')
      Producto.objects.create( nombre = nombre, precio = precio, categoria = categoria, stockActual = stockactual, proveedor_id=proveedor)
      return redirect ('mostrarprod')
    return render(request, 'compra/registrarproducto.html')
   

#Muestra todos los proveedores
class mostrarProv(generic.ListView):
   model = Proveedor
   paginate_by = 10

def registrarProv(request):
    if request.method == 'POST':
      nombre = request.POST.get('nombre')
      apellido = request.POST.get('apellido')
      dni = request.POST.get('dni')
      provincia = request.POST.get('provincia')
      Proveedor.objects.create( nombre = nombre, apellido = apellido, dni = dni, provincia = provincia)
      return redirect ('mostrarprov')
    return render(request, 'compra/registraroroveedor.html')