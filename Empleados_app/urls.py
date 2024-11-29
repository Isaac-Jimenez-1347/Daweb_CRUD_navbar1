from django.urls import path
from Empleados_app import views

urlpatterns = [
    path('empleados', views.inicio_vistaEmpleados, name="empleados"),
    path('registrarEmpleado/', views.registrarEmpleados, name="registrarEmpleados"),
    path('borrarEmpleado/<id_empleado>/', views.borrarEmpleados, name="borrarEmpleados"),
    path('seleccionarEmpleado/<id_empleado>/', views.seleccionarEmpleados, name="seleccionarEmpleados"),
    path('editarEmpleado/', views.editarEmpleados, name="editarEmpleados"),
]
