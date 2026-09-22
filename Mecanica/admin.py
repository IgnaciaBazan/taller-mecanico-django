from django.contrib import admin
from .models import Marca, Cliente, Vehiculo, Servicio, OrdenTrabajo
# Register your models here.


@admin.register(Marca)
class MarcaAdmin(admin.ModelAdmin):
    list_display = ("nombre",)
    search_fields = ("nombre",)
    ordering = ("nombre",)


@admin.register(Servicio)
class ServicioAdmin(admin.ModelAdmin):
    list_display = ("nombre", "precio")
    search_fields = ("nombre",)
    ordering = ("nombre",)

@admin.register(OrdenTrabajo)
class OrdenTrabajoAdmin(admin.ModelAdmin):
    list_display = ("id", "vehiculo", "fecha_ingreso", "estado")
    list_filter = ("estado", "fecha_ingreso")
    search_fields = ("vehiculo__patente", "vehiculo__modelo", "vehiculo__cliente__nombres", "vehiculo__cliente__apellidos")
    ordering = ("-fecha_ingreso",)


@admin.register(Vehiculo)
class VehiculoAdmin(admin.ModelAdmin):
    list_display = ("patente", "marca", "modelo", "anio", "kilometraje", "cliente")
    list_filter = ("marca", "anio")
    search_fields = ("patente", "modelo", "cliente__nombres", "cliente__apellidos")
    ordering = ("patente",)


@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ("nombres", "apellidos", "rut", "email", "telefono")
    search_fields = ("nombres", "apellidos", "rut")
    ordering = ("apellidos", "nombres")
    list_filter = ("apellidos", "nombres")  
