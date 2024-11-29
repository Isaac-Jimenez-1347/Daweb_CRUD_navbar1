from django.urls import path
from Pedidos_app import views

urlpatterns = [
    path('pedidos', views.inicio_vistaPedidos, name="pedidos"),
    path('registrarPedido/', views.registrarPedidos, name="registrarPedidos"),
    path('borrarPedido/<id_pedido>/', views.borrarPedidos, name="borrarPedidos"),
    path('seleccionarPedido/<id_pedido>/', views.seleccionarPedidos, name="seleccionarPedidos"),
    path('editarPedido/', views.editarPedidos, name="editarPedidos"),
]
