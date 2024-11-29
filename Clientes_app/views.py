from django.shortcuts import render, redirect
from .models import Clientes

def inicio_vistaClientes(request):
    losclientes = Clientes.objects.all() 
    return render(request, "gestionarClientes.html", {"misclientes": losclientes})


def registrarClientes(request):
    if request.method == "POST":
        id_cliente = request.POST["txtcodigo"]
        nombre = request.POST["txtnombre"]
        apellido_p = request.POST["txtapellido_p"]
        apellido_m = request.POST["txtapellido_m"]
        fecha_nac = request.POST["txtfecha_nac"]
        email = request.POST["txtemail"]
        celular = request.POST["txtcelular"]
        
        guardarclientes = Clientes.objects.create(
            id_cliente=id_cliente,
            nombre=nombre,
            apellido_p=apellido_p,
            apellido_m=apellido_m,
            fecha_nac=fecha_nac,
            email=email,
            celular=celular
        )
        return redirect("clientes")

def seleccionarClientes(request, id_cliente):
    clientes = Clientes.objects.get(id_cliente=id_cliente)
    return render(request, "editarClientes.html", {"misclientes": clientes})

def editarClientes(request):
    if request.method == "POST":

        id_cliente = request.POST["txtcodigo"]
        nombre = request.POST["txtnombre"]
        apellido_p = request.POST["txtapellido_p"]
        apellido_m = request.POST["txtapellido_m"]
        fecha_nac = request.POST["txtfecha_nac"]
        email = request.POST["txtemail"]
        celular = request.POST["txtcelular"]
        
        clientes = Clientes.objects.get(id_cliente=id_cliente)
        clientes.nombre = nombre
        clientes.apellido_p = apellido_p
        clientes.apellido_m = apellido_m
        clientes.fecha_nac = fecha_nac
        clientes.email = email
        clientes.celular = celular
        
        clientes.save()
        return redirect("clientes")

def borrarClientes(request, id_cliente):
    clientes = Clientes.objects.get(id_cliente=id_cliente)
    clientes.delete()
    return redirect("clientes")


