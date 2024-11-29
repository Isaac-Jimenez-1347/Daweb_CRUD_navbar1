from django.shortcuts import render, redirect
from .models import Empleados

def inicio_vistaEmpleados(request):
    losempleados = Empleados.objects.all()
    return render(request, "gestionarEmpleados.html", {"misempleados": losempleados})

def registrarEmpleados(request):
    if request.method == "POST":
        id_empleado = request.POST["txtcodigo"]
        nombre = request.POST["txtnombre"]
        apellido_p = request.POST["txtapellido_p"]
        apellido_m = request.POST["txtapellido_m"]
        genero = request.POST["txtgenero"]
        matricula = request.POST["txtmatricula"]
        celular = request.POST["txtcelular"]
        puesto = request.POST["txtpuesto"]
        salario = request.POST["txtsalario"]

        # Crear el empleado
        Empleados.objects.create(
            id_empleado=id_empleado,
            nombre=nombre,
            apellido_p=apellido_p,
            apellido_m=apellido_m,
            genero=genero,
            matricula=matricula,
            celular=celular,
            puesto=puesto,
            salario=salario
        )
        return redirect("empleados")

def seleccionarEmpleados(request, id_empleado):
    try:
        empleado = Empleados.objects.get(id_empleado=id_empleado)
    except Empleados.DoesNotExist:
        return redirect("empleados")  # En caso de que no exista el empleado
    return render(request, "editarEmpleados.html", {"misempleados": empleado})

def editarEmpleados(request):
    if request.method == "POST":
        id_empleado = request.POST["txtcodigo"]
        nombre = request.POST["txtnombre"]
        apellido_p = request.POST["txtapellido_p"]
        apellido_m = request.POST["txtapellido_m"]
        genero = request.POST["txtgenero"]
        matricula = request.POST["txtmatricula"]
        celular = request.POST["txtcelular"]
        puesto = request.POST["txtpuesto"]
        salario = request.POST["txtsalario"]

        try:
            empleado = Empleados.objects.get(id_empleado=id_empleado)
            empleado.nombre = nombre
            empleado.apellido_p = apellido_p
            empleado.apellido_m = apellido_m
            empleado.genero = genero
            empleado.matricula = matricula
            empleado.celular = celular
            empleado.puesto = puesto
            empleado.salario = salario
            empleado.save()
        except Empleados.DoesNotExist:
            return redirect("empleados")  # En caso de que no exista el empleado

        return redirect("empleados")

def borrarEmpleados(request, id_empleado):
    try:
        empleado = Empleados.objects.get(id_empleado=id_empleado)
        empleado.delete()
    except Empleados.DoesNotExist:
        pass  # Si no existe, no hacemos nada

    return redirect("empleados")
