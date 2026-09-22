from django.urls import path
from . import views

urlpatterns = [
    path("", views.inicio, name ="inicio"),
    
    path("vehiculos/", views.listar_vehiculos, name="listar_vehiculos"),
    path("vehiculos/nuevo/", views.crear_vehiculo, name="crear_vehiculo"),
    path("vehiculos/<str:patente>/editar/", views.editar_vehiculo, name="editar_vehiculo"), 
    path("vehiculos/<str:patente>/eliminar/", views.eliminar_vehiculo, name="eliminar_vehiculo"),

    path("ordenes/", views.listar_ordenes, name="listar_ordenes"),
    path("ordenes/nuevo/", views.crear_orden, name="crear_orden"),
    path("ordenes/<int:id>/editar/", views.editar_orden, name="editar_orden"),
    path("ordenes/<int:id>/eliminar/", views.eliminar_orden, name="eliminar_orden"),

]