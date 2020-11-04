from django.contrib import admin
from django.conf.urls import url
from django.urls import path, include

from . import views

urlpatterns = [
    path('index',views.index, name='index'),
    path('listar',views.listar, name='listar'),
    path('mostrar_productos',views.mostrar_productos, name='mostrar_productos'),
    path('boton_buscar',views.boton_buscar, name='boton_buscar'),
    path('buscar_por_id',views.buscar_por_id, name='buscar_por_id'),
    path('eliminar',views.eliminar, name='eliminar'),
    path('eliminar_por_id',views.eliminar_por_id, name='eliminar_por_id'),
    path('agregar',views.agregar, name='agregar'),
    path('agregar_producto', views.agregar_producto, name='agregar_producto'),
    path('editar',views.editar, name='editar'),
    path('buscar_para_editar', views.buscar_para_editar, name='buscar_para_editar'),
    path('actualizar_producto',views.actualizar_producto, name='actualizar_producto'),
    path('Inicio',views.Inicio, name='Inicio'),
    path('Bebidas',views.Bebidas, name='Bebidas'),
    path('Snack',views.Snack, name='Snack'),
    path('Cabritas',views.Cabritas, name='Cabritas'),
    path('listar_productos',views.listar_productos, name='listar_productos'),
    path('administrar',views.administrar, name='administrar'),





]