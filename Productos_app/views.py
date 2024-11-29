from django.shortcuts import render, redirect
from .models import Productos

def inicio_vistaProductos(request):
    losproductos = Productos.objects.all()
    return render(request, "gestionarProductos.html", {"misproductos": losproductos})

def registrarProductos(request):
    if request.method == "POST":
        id_producto = request.POST["txtcodigo"]
        nombre = request.POST["txtnombre"]
        tipo = request.POST["txttipo"]
        descripcion = request.POST["txtdescripcion"]
        color = request.POST["txtcolor"]
        material = request.POST["txtmaterial"]
        precio = request.POST["txtprecio"]
        id_sucursal = request.POST["txtid_sucursal"]
        id_provedor = request.POST["txtid_provedor"]

        # Crear el producto
        Productos.objects.create(
            id_producto=id_producto,
            nombre=nombre,
            tipo=tipo,
            descripcion=descripcion,
            color=color,
            material=material,
            precio=precio,
            id_sucursal=id_sucursal,
            id_provedor=id_provedor
        )
        return redirect("productos")

def seleccionarProductos(request, id_producto):
    try:
        producto = Productos.objects.get(id_producto=id_producto)
    except Productos.DoesNotExist:
        return redirect("productos")  # En caso de que no exista el producto
    return render(request, "editarProductos.html", {"misproductos": producto})

def editarProductos(request):
    if request.method == "POST":
        id_producto = request.POST["txtcodigo"]
        nombre = request.POST["txtnombre"]
        tipo = request.POST["txttipo"]
        descripcion = request.POST["txtdescripcion"]
        color = request.POST["txtcolor"]
        material = request.POST["txtmaterial"]
        precio = request.POST["txtprecio"]
        id_sucursal = request.POST["txtid_sucursal"]
        id_provedor = request.POST["txtid_provedor"]

        try:
            producto = Productos.objects.get(id_producto=id_producto)
            producto.nombre = nombre
            producto.tipo = tipo
            producto.descripcion = descripcion
            producto.color = color
            producto.material = material
            producto.precio = precio
            producto.id_sucursal = id_sucursal
            producto.id_provedor = id_provedor
            producto.save()
        except Productos.DoesNotExist:
            return redirect("productos")  # En caso de que no exista el producto

        return redirect("productos")

def borrarProductos(request, id_producto):
    try:
        producto = Productos.objects.get(id_producto=id_producto)
        producto.delete()
    except Productos.DoesNotExist:
        pass  # Si no existe, no hacemos nada

    return redirect("productos")
