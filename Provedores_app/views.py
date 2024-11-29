from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .models import Provedor

def registrarProvedor(request):
    if request.method == "POST":
        id_provedor = request.POST["txtid_provedor"]
        nombre_empresa = request.POST["txtnombre_empresa"]
        fecha = request.POST["txtfecha"]
        horarios = request.POST["txthorarios"]
        email = request.POST["txtemail"]
        celular = request.POST["txtcelular"]
        direccion = request.POST["txtdireccion"]
        codigo_postal = request.POST["txtcodigo_postal"]

        # Crear un nuevo proveedor
        Provedor.objects.create(
            id_provedor=id_provedor,
            nombre_empresa=nombre_empresa,
            fecha=fecha,
            horarios=horarios,
            email=email,
            celular=celular,
            direccion=direccion,
            codigo_postal=codigo_postal
        )
        return redirect("proveedores")
def inicio_vistaProvedores(request):
    losprovedores = Provedor.objects.all()  # Obtener todos los proveedores
    return render(request, "gestionarProvedores.html", {"misprovedores": losprovedores})
def seleccionarProvedor(request, id_provedor):
    try:
        provedor = Provedor.objects.get(id_provedor=id_provedor)
    except Provedor.DoesNotExist:
        return redirect("proveedores")  # En caso de que no exista el proveedor
    return render(request, "editarProvedor.html", {"misprovedores": provedor})
def editarProvedor(request):
    if request.method == "POST":
        id_provedor = request.POST["txtid_provedor"]
        nombre_empresa = request.POST["txtnombre_empresa"]
        fecha = request.POST["txtfecha"]
        horarios = request.POST["txthorarios"]
        email = request.POST["txtemail"]
        celular = request.POST["txtcelular"]
        direccion = request.POST["txtdireccion"]
        codigo_postal = request.POST["txtcodigo_postal"]

        try:
            provedor = Provedor.objects.get(id_provedor=id_provedor)
            provedor.nombre_empresa = nombre_empresa
            provedor.fecha = fecha
            provedor.horarios = horarios
            provedor.email = email
            provedor.celular = celular
            provedor.direccion = direccion
            provedor.codigo_postal = codigo_postal
            provedor.save()
        except Provedor.DoesNotExist:
            return redirect("proveedores")  # En caso de que no exista el proveedor

        return redirect("proveedores")
def borrarProvedor(request, id_provedor):
    try:
        provedor = Provedor.objects.get(id_provedor=id_provedor)
        provedor.delete()
    except Provedor.DoesNotExist:
        pass  # Si no existe el proveedor, no hacemos nada

    return redirect("proveedores")

