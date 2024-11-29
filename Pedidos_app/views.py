from django.shortcuts import render, redirect
from .models import Pedidos

def inicio_vistaPedidos(request):
    lospedidos = Pedidos.objects.all()
    return render(request, "gestionarPedidos.html", {"mispedidos": lospedidos})

def registrarPedidos(request):
    if request.method == "POST":
        id_pedido = request.POST["txtcodigo"]
        nombre = request.POST["txtnombre"]
        fecha = request.POST["txtfecha"]
        hora = request.POST["txthora"]
        id_producto = request.POST["txtid_producto"]
        id_cliente = request.POST["txtid_cliente"]
        cantidad = request.POST["txtcantidad"]
        id_trabajador = request.POST["txtid_trabajador"]
        registro = request.POST["txtregistro"]

        # Crear el pedido
        Pedidos.objects.create(
            id_pedido=id_pedido,
            nombre=nombre,
            fecha=fecha,
            hora=hora,
            id_producto=id_producto,
            id_cliente=id_cliente,
            cantidad=cantidad,
            id_trabajador=id_trabajador,
            registro=registro
        )
        return redirect("pedidos")

def seleccionarPedidos(request, id_pedido):
    try:
        pedido = Pedidos.objects.get(id_pedido=id_pedido)
    except Pedidos.DoesNotExist:
        return redirect("pedidos")  # En caso de que no exista el pedido
    return render(request, "editarPedidos.html", {"mispedidos": pedido})

def editarPedidos(request):
    if request.method == "POST":
        id_pedido = request.POST["txtcodigo"]
        nombre = request.POST["txtnombre"]
        fecha = request.POST["txtfecha"]
        hora = request.POST["txthora"]
        id_producto = request.POST["txtid_producto"]
        id_cliente = request.POST["txtid_cliente"]
        cantidad = request.POST["txtcantidad"]
        id_trabajador = request.POST["txtid_trabajador"]
        registro = request.POST["txtregistro"]

        try:
            pedido = Pedidos.objects.get(id_pedido=id_pedido)
            pedido.nombre = nombre
            pedido.fecha = fecha
            pedido.hora = hora
            pedido.id_producto = id_producto
            pedido.id_cliente = id_cliente
            pedido.cantidad = cantidad
            pedido.id_trabajador = id_trabajador
            pedido.registro = registro
            pedido.save()
        except Pedidos.DoesNotExist:
            return redirect("pedidos")  # En caso de que no exista el pedido

        return redirect("pedidos")

def borrarPedidos(request, id_pedido):
    try:
        pedido = Pedidos.objects.get(id_pedido=id_pedido)
        pedido.delete()
    except Pedidos.DoesNotExist:
        pass  # Si no existe, no hacemos nada

    return redirect("pedidos")
