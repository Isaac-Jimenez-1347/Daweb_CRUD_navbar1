from django.urls import path
from Clientes_app import views

urlpatterns = [
    path('clientes', views.inicio_vistaClientes, name="clientes"),
    path('registrarCliente/', views.registrarClientes, name="registrarClientes"),  
    path('borrarCliente/<id_cliente>/', views.borrarClientes, name="borrarClientes"), 
    path('seleccionarCliente/<id_cliente>/', views.seleccionarClientes, name="seleccionarClientes"),
    path('editarClientes/', views.editarClientes, name="editarClientes"),  
]
