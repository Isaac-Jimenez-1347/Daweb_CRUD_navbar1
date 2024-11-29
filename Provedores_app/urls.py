from django.urls import path
from Provedores_app import views

urlpatterns = [
    path('proveedores', views.inicio_vistaProvedores, name="proveedores"),
    path('registrarProvedor/', views.registrarProvedor, name="registrarProvedor"),
    path('borrarProvedor/<id_provedor>/', views.borrarProvedor, name="borrarProvedor"),
    path('seleccionarProvedor/<id_provedor>/', views.seleccionarProvedor, name="seleccionarProvedor"),
    path('editarProvedor/', views.editarProvedor, name="editarProvedor"),
]
