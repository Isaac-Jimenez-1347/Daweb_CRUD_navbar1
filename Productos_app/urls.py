from django.urls import path
from Productos_app import views

urlpatterns = [
    path('productos', views.inicio_vistaProductos, name="productos"),
    path('registrarProducto/', views.registrarProductos, name="registrarProductos"),
    path('borrarProducto/<id_producto>/', views.borrarProductos, name="borrarProductos"),
    path('seleccionarProducto/<id_producto>/', views.seleccionarProductos, name="seleccionarProductos"),
    path('editarProducto/', views.editarProductos, name="editarProductos"),
]
