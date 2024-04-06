from django.urls import path
from . import views 

urlpatterns = [
    path('regristrarproducto/', views.registrarProd),
    path('regristrarProv/', views.registrarProv),
    path('mostrarproductos/',views.mostrarProd),
    path('filtrarproductos/<char:categoria>',views.mostrarProdfiltrados),
    path('actualizarproductos/',views.actualizarProd),
    path('borrarproductos/', views.borrarProd),
    path('mostrarprov/',views.mostrarProv)
]