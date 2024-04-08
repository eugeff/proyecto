from django.shortcuts import render, redirect, get_list_or_404, get_object_or_404
from .models import Producto, Proveedor
from django.http import HttpResponse,Http404
from django.views import generic
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
        'miApp/index.html',
        context={'numProd':numProd,'numProv':numProv,'numProdEle':numProdEle,'numProdElectrodom':numProdElectrodom,'numProdHo':numProdHo,'numProdDe':numProdDe},)





#Muestra todos los productos 
class mostrarProd(generic.ListView):
   model = Producto
   paginate_by = 10


#Muestra productos  filtrados por categoria 
def prodFiltrados(request,nombre):
    try:
        prodcategoria=Producto.objects.get(nombre = nombre)
    except Producto.DoesNotExist:
        raise Http404("Ese producto no se encuentra listado")
    return render(
        request,
        'miApp/prodFiltrados.html',
        context={'producto':prodcategoria,}
    )


# Formulario para registrar producto
def registrarProd(request):
    if request.method == 'POST':
      nombre = request.POST.get('nombre')
      precio = request.POST.get('precio')
      categoria = request.POST.get('categoria')
      stockactual = request.POST.get('stockactual')
      proveedor  = request.POST.get('proveedor')
      Producto.objects.create( nombre = nombre, precio = precio, categoria = categoria, stockactual = stockactual, proveedor=proveedor)
      return redirect ('mostrarProd')
    return render(request, 'miApp/registrarproducto.html')
   
   

def actualizarProd(request,nombre):
   prodEncontrado = get_object_or_404(Producto, nombre = nombre)
   if request.method == 'POST':
      precio = request.POST.get('precio')
      stockactual = request.POST.get('stockactual')
      proveedor = request.POST.get('proveedor')
      Producto.precio = precio
      Producto.stockActual = stockactual
      Producto.proveedor = proveedor
      Producto.save()
      return redirect('mostrarProd')
   return render(request, 'miApp/actualizarproducto.html', {'Producto': Producto})


def borrarProd(request, nombre):
    producto = get_object_or_404(Producto, nombre=nombre)
    if request.method == 'POST':
        producto.delete()
        return redirect('mostrarProd')
    return render(request, 'miApp/borrarproductos.html', {'producto': producto})



#Muestra todos los proveedores
def mostrarProv(request):
   proveedor=Proveedor.objects.all()
   return render(
      request,
      'miApp/mostrarProveedor.html', 
      {'proveedor':proveedor}
      )


def registrarProv(request):
    if request.method == 'POST':
      nombre = request.POST.get('nombre')
      apellido = request.POST.get('apellido')
      dni = request.POST.get('dni')
      provincia = request.POST.get('provincia')
      Proveedor.objects.create( nombre = nombre, apellido = apellido, dni = dni, provincia = provincia)
      return redirect ('mostrarProv')
    return render(request, 'miApp/registraroroveedor.html')