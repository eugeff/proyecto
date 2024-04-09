from django.urls import path
from . import views 

urlpatterns = [
    path('', views.index, name='index'),
    path('registrarproducto/', views.registrarProd,name='registrarprod'),
    path('registrarProv/', views.registrarProv,name='registrarprov'),
    path('mostrarproductos/',views.mostrarProd.as_view(),name='mostrarprod'),
    path('mostrarprov/',views.mostrarProv.as_view(),name = 'mostrarprov')
]