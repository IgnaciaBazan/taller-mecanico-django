from django.db import models

# Create your models here.


class Marca(models.Model):
    nombre = models.CharField(max_length=50, unique=True)

    class Meta:
        ordering = ["nombre"]

    def __str__(self):
        return self.nombre


class Cliente(models.Model):
    rut = models.CharField(max_length=12, unique = True)
    nombres = models.CharField(max_length=50)
    apellidos = models.CharField(max_length= 50)
    telefono = models.CharField(max_length=15)
    email= models.EmailField(blank=True)

    class Meta:
        ordering = ["apellidos", "nombres"]

    def __str__(self):
        return f"{self.nombres} {self.apellidos}"

class Vehiculo(models.Model):
    patente= models.CharField(max_length=8, primary_key=True)
    marca = models.ForeignKey(Marca, on_delete=models.PROTECT, related_name="vehiculos")
    cliente = models.ForeignKey(Cliente, on_delete=models.PROTECT, related_name="vehiculos")
    modelo = models.CharField(max_length=50)
    anio= models.PositiveIntegerField()
    kilometraje = models.PositiveIntegerField(default=0)

    class Meta:
        ordering= ["marca", "patente"]

    def __str__(self):
        return f"{self.patente} {self.modelo}"

class Servicio(models.Model):
    nombre= models.CharField(max_length=80)
    descripcion = models.TextField(blank=True)
    precio = models.DecimalField(max_digits=8, decimal_places=0)

    class Meta:
        ordering= ["nombre"]

    def __str__(self):
        return self.nombre

class OrdenTrabajo(models.Model):
    ESTADO_CHOICES = [
        ("pendiente", "Pendiente"),
        ("en_proceso", "En proceso"),
        ("listo", "Listo para retiro"),
        ("entregado", "Entregado"),
    ]

    vehiculo= models.ForeignKey(Vehiculo, on_delete=models.CASCADE, related_name="ordenes")
    servicios= models.ManyToManyField(Servicio, blank=True, related_name="ordenes")
    fecha_ingreso= models.DateField(auto_now_add=True)
    fecha_entrega_estimada= models.DateField(null=True, blank=True)
    estado= models.CharField(max_length=15, choices=ESTADO_CHOICES, default="pendiente")
    kilometraje_ingreso= models.PositiveIntegerField()
    observaciones = models.TextField(blank=True) 


    class Meta:
        ordering= ["-fecha_ingreso"]

    def __str__(self):
        return f"Orden #{self.pk} - {self.vehiculo}"