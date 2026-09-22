
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from .models import Vehiculo, Cliente, Marca, OrdenTrabajo, Servicio
from django.db import IntegrityError
# Create your views here.


@login_required
def inicio(request):
    return render(request, "Mecanica/inicio.html")


@login_required
def listar_vehiculos(request):
    vehiculos = Vehiculo.objects.all()
    return render(request, "Mecanica/listar_vehiculos.html", {"vehiculos": vehiculos})

@login_required
def crear_vehiculo(request):
    if request.method == "POST":
        try:
            Vehiculo.objects.create(
                patente=request.POST.get("patente"),
                marca_id=request.POST.get("marca"),
                modelo=request.POST.get("modelo"),
                anio=request.POST.get("anio"),
                kilometraje=request.POST.get("kilometraje"),
                cliente_id=request.POST.get("cliente")
            )
            return redirect("listar_vehiculos")
        except IntegrityError:
            error_message = "La patente ya existe. Por favor, ingrese una patente única."
            clientes = Cliente.objects.all()
            marcas = Marca.objects.all()
            return render(request, "Mecanica/crear_vehiculo.html", {
                "clientes": Cliente.objects.all(),
                "marcas": Marca.objects.all(),
                "error": error_message,
            })

    clientes = Cliente.objects.all()
    marcas = Marca.objects.all()
    return render(request, "Mecanica/crear_vehiculo.html", {"clientes": clientes, "marcas": marcas})


@login_required
def eliminar_vehiculo(request, patente):
    vehiculo = get_object_or_404(Vehiculo, patente=patente)
    if request.method == "POST":
        vehiculo.delete()
        return redirect("listar_vehiculos")
    return render(request, "Mecanica/eliminar_vehiculo.html", {"vehiculo": vehiculo})

@login_required
def editar_vehiculo(request, patente):
    vehiculo = get_object_or_404(Vehiculo, patente=patente)
    if request.method == "POST":
        vehiculo.marca_id = request.POST.get("marca")
        vehiculo.modelo = request.POST.get("modelo")
        vehiculo.anio = request.POST.get("anio")
        vehiculo.kilometraje = request.POST.get("kilometraje")
        vehiculo.cliente_id = request.POST.get("cliente")
        vehiculo.save()
        return redirect("listar_vehiculos")

    clientes = Cliente.objects.all()
    marcas = Marca.objects.all()
    return render(request, "Mecanica/editar_vehiculo.html", {"vehiculo": vehiculo, "clientes": clientes, "marcas": marcas})     
    


@login_required
def listar_ordenes(request):
    ordenes = OrdenTrabajo.objects.select_related("vehiculo", "vehiculo__cliente").all()

    cliente_id = request.GET.get("cliente")
    if cliente_id:
        ordenes = ordenes.filter(vehiculo__cliente_id=cliente_id)

    contexto = {
        "ordenes": ordenes,
        "clientes": Cliente.objects.all(),
        "cliente_seleccionado": cliente_id,

    }
    return render(request, "Mecanica/listar_ordenes.html", contexto)


@login_required
def eliminar_orden(request, id):
    orden = get_object_or_404(OrdenTrabajo, pk=id)
    if request.method == "POST":
        orden.delete()
        return redirect("listar_ordenes")
    return render(request, "Mecanica/eliminar_orden.html", {"orden": orden})


@login_required
def crear_orden(request):
    if request.method == "POST":
        orden = OrdenTrabajo.objects.create(
            vehiculo_id=request.POST.get("vehiculo"),
            kilometraje_ingreso=request.POST.get("kilometraje"),
            fecha_entrega_estimada=request.POST.get("fecha_entrega_estimada") or None,
            observaciones=request.POST.get("observaciones", ""),

        )
        servicios_ids = request.POST.getlist("servicios")
        orden.servicios.set(servicios_ids)
        return redirect("listar_ordenes")

    vehiculos = Vehiculo.objects.all()
    servicios = Servicio.objects.all()
    return render(request, "Mecanica/crear_orden.html", {"vehiculos": vehiculos, "servicios": servicios})



@login_required
def editar_orden(request, id):
    orden = get_object_or_404(OrdenTrabajo, pk=id)
    if request.method == "POST":
        orden.vehiculo_id = request.POST.get("vehiculo")
        orden.kilometraje_ingreso = request.POST.get("kilometraje")
        orden.fecha_entrega_estimada = request.POST.get("fecha_entrega_estimada") or None
        orden.observaciones = request.POST.get("observaciones", "")
        orden.estado = request.POST.get("estado")
        servicios_ids = request.POST.getlist("servicios")
        orden.servicios.set(servicios_ids)
        orden.save()
        return redirect("listar_ordenes")

    vehiculos = Vehiculo.objects.all()
    servicios = Servicio.objects.all()
    return render(request, "Mecanica/editar_orden.html", {"orden": orden, "vehiculos": vehiculos, "servicios": servicios, "estados": OrdenTrabajo.ESTADO_CHOICES})