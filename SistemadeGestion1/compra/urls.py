from django.urls import path
from . import views 

urlpatterns = [
    path('', views.index, name='index'),
    path('registrarproducto/', views.registrarProd),
    path('registrarProv/', views.registrarProv),
    path('mostrarproductos/',views.mostrarProd.as_view(),name='mostrarprod'),
    path('producto/<str:nombre>',views.prodFiltrados,name='prodfiltrados'),
    path('actualizarproductos/',views.actualizarProd),
    path('borrarproductos/', views.borrarProd),
    path('mostrarprov/',views.mostrarProv)
]