from django.shortcuts import render, redirect
from .models import Sucursal

def inicio_vistaSucursales(request):
    lossucursales = Sucursal.objects.all()
    return render(request, "gestionarSucursales.html", {"missucursales": lossucursales})

def registrarSucursales(request):
    if request.method == "POST":
        id_sucursal = request.POST["txtcodigo"]
        nombre = request.POST["txtnombre"]
        ubicacion = request.POST["txtubicacion"]
        horarios = request.POST["txthorarios"]
        email = request.POST["txtemail"]
        celular = request.POST["txtcelular"]
        id_empleado = request.POST["txtid_empleado"]

        # Crear la sucursal
        Sucursal.objects.create(
            id_sucursal=id_sucursal,
            nombre=nombre,
            ubicacion=ubicacion,
            horarios=horarios,
            email=email,
            celular=celular,
            id_empleado=id_empleado
        )
        return redirect("sucursales")

def seleccionarSucursales(request, id_sucursal):
    try:
        sucursal = Sucursal.objects.get(id_sucursal=id_sucursal)
    except Sucursal.DoesNotExist:
        return redirect("sucursales")  # En caso de que no exista la sucursal
    return render(request, "editarSucursales.html", {"missucursales": sucursal})

def editarSucursales(request):
    if request.method == "POST":
        id_sucursal = request.POST["txtcodigo"]
        nombre = request.POST["txtnombre"]
        ubicacion = request.POST["txtubicacion"]
        horarios = request.POST["txthorarios"]
        email = request.POST["txtemail"]
        celular = request.POST["txtcelular"]
        id_empleado = request.POST["txtid_empleado"]

        try:
            sucursal = Sucursal.objects.get(id_sucursal=id_sucursal)
            sucursal.nombre = nombre
            sucursal.ubicacion = ubicacion
            sucursal.horarios = horarios
            sucursal.email = email
            sucursal.celular = celular
            sucursal.id_empleado = id_empleado
            sucursal.save()
        except Sucursal.DoesNotExist:
            return redirect("sucursales")  # En caso de que no exista la sucursal

        return redirect("sucursales")

def borrarSucursales(request, id_sucursal):
    try:
        sucursal = Sucursal.objects.get(id_sucursal=id_sucursal)
        sucursal.delete()
    except Sucursal.DoesNotExist:
        pass  # Si no existe, no hacemos nada

    return redirect("sucursales")
