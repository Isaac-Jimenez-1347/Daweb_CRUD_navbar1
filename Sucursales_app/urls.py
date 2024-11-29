from django.urls import path
from Sucursales_app import views

urlpatterns = [
    path('sucursales', views.inicio_vistaSucursales, name="sucursales"),
    path('registrarSucursal/', views.registrarSucursales, name="registrarSucursales"),
    path('borrarSucursal/<id_sucursal>/', views.borrarSucursales, name="borrarSucursales"),
    path('seleccionarSucursal/<id_sucursal>/', views.seleccionarSucursales, name="seleccionarSucursales"),
    path('editarSucursal/', views.editarSucursales, name="editarSucursales"),
]
