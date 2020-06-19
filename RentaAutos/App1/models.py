from decimal import Decimal
import shortuuid
from django.core.validators import RegexValidator, MinValueValidator
from django.forms import IntegerField
from django.utils import timezone
from django.db import models

# Create your models here.
from .Validaciones import validar_vehiculo_rentado, validar_digito_verificador


def generar_numero_renta():
    return  shortuuid.ShortUUID().random(length=7)

class TiposVehiculos(models.Model):
    descripcion = models.CharField(max_length=300)
    estado = models.BooleanField(default=False)

    def __str__(self):
        return self.descripcion
    class Meta:
        verbose_name="Tipo de vehiculo"
        verbose_name_plural="Tipos de vehiculos"

class Marcas(models.Model):
    descripcion = models.CharField(max_length=200)
    estado = models.BooleanField(default=False)

    def __str__(self):
        return self.descripcion
    class Meta:
        verbose_name="Marca"
        verbose_name_plural="Marcas"

class Modelo(models.Model):
    descripcion = models.CharField(max_length=200)
    estado = models.BooleanField(default=False)
    marca = models.ForeignKey('Marcas', on_delete=models.CASCADE,)

    def __str__(self):
        return self.descripcion
    class Meta:
        verbose_name="Modelo"
        verbose_name_plural="Modelos"

class TiposCombustible(models.Model):
    descripcion = models.CharField(max_length=200)
    estado = models.BooleanField(default=False)

    def __str__(self):
        return self.descripcion
    class Meta:
        verbose_name="Tipo de combustible"
        verbose_name_plural="Tipos de combustibles"

class Vehiculos(models.Model):
    descripcion = models.CharField(max_length=200)
    chasis = models.IntegerField(validators=[MinValueValidator(1)])
    motor = models.CharField(max_length=50)
    placa = models.CharField(max_length=50)
    tipo_de_vehiculo = models.ForeignKey('TiposVehiculos', on_delete=models.CASCADE,)
    marca = models.ForeignKey('Marcas', on_delete=models.CASCADE, )
    modelo = models.ForeignKey('Modelo', on_delete=models.CASCADE, )
    tipo_de_combustible = models.ForeignKey('TiposCombustible', on_delete=models.CASCADE, )
    estado = models.BooleanField(default=True)
    imagen_vehiculo = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.descripcion
    class Meta:
        verbose_name="Vehiculo"
        verbose_name_plural="Vehiculos"

class Clientes(models.Model):
    nombre = models.CharField(max_length=100)
    cedula = models.CharField(max_length=13, unique=True, validators=[validar_digito_verificador ,RegexValidator(regex=r"^\d{3}-\d{7}-\d$",message="Cedula y guiones Ex:(001-0000000-1)")])
    tarejeta_de_credito = models.CharField(max_length=20)
    limite_de_credito = models.IntegerField(validators=[MinValueValidator(1),])
    tipo_de_persona_choices = [
        ('Jur', 'Juridica'),
        ('Fis', 'Fisica')
    ]
    tipo_de_persona = models.CharField(max_length=10, choices=tipo_de_persona_choices)
    estado = models.BooleanField(default=False)

    def __str__(self):
        return self.nombre
    class Meta:
        verbose_name="Cliente"
        verbose_name_plural="Clientes"

class Empleados(models.Model):
    nombre = models.CharField(max_length=100)
    cedula = models.CharField(max_length=13, unique=True, validators=[validar_digito_verificador, RegexValidator(regex=r"^\d{3}-\d{7}-\d$",message="Cedula y guiones Ex:(001-0000000-1)")])
    tanda_labor_choices =[
        ('Mat', 'Matutina'),
        ('Ves', 'Vespertina'),
        ('Noc', 'Nocturna')
    ]
    tanda_labor = models.CharField(max_length=3, choices=tanda_labor_choices)
    comision = models.CharField(max_length=50)
    fecha_de_ingreso = models.DateTimeField(default=timezone.now)
    estado = models.BooleanField(default=False)

    def __str__(self):
        return self.nombre
    class Meta:
        verbose_name="Empleado"
        verbose_name_plural="Empleados"

class Inspeccion(models.Model):
    ralladura = models.BooleanField(default=False)
    rotura_de_cristal = models.BooleanField(default=False)
    goma_de_repuesto = models.BooleanField(default=False)
    tiene_gato = models.BooleanField(default=False)
    cantidad_combustible_choices = (
        ('25%', '1/4'),
        ('50%', '1/2'),
        ('75%', '3/4'),
        ('100%', 'Full')
    )
    cantidad_de_combustible = models.CharField(max_length=4, choices=cantidad_combustible_choices)
    estado_de_gomas = models.BooleanField(default=False)
    fecha = models.DateField(default=timezone.now)
    estado = models.CharField(max_length=100)
    empleado_de_inspeccion = models.ForeignKey('Empleados', on_delete=models.CASCADE,)
    vehiculo = models.ForeignKey('Vehiculos', on_delete=models.CASCADE,)
    cliente = models.ForeignKey('Clientes', on_delete=models.CASCADE,)


    def __str__(self):
        return str(self.fecha)
    class Meta:
        verbose_name="Inspeccion"
        verbose_name_plural="Inspecciones"


class Renta_devolucion (models.Model):
    # Numero_de_renta = models.IntegerField(unique=True, validators=[MinValueValidator(1)])
    numero_renta = models.CharField(max_length=50, default=generar_numero_renta)

    def __str__(self):
        return (self.numero_renta)

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        if self.pk is None:
            self.vehiculo.estado = False
            self.vehiculo.save()
        super(Renta_devolucion, self).save(force_insert, force_update, using, update_fields)

    fecha_de_Renta = models.DateTimeField(default= timezone.now)
    fecha_de_Devuelta = models.DateTimeField(blank=True, null=True)
    monto_por_dia = models.FloatField(validators=[MinValueValidator(1),])
    cantidad_de_Dia = models.IntegerField(validators=[MinValueValidator(1),])
    empleado = models.ForeignKey('Empleados', on_delete=models.CASCADE, )
    vehiculo = models.ForeignKey('Vehiculos', on_delete=models.CASCADE, validators=[validar_vehiculo_rentado] )
    cliente = models.ForeignKey('Clientes', on_delete=models.CASCADE, )
    estado = models.BooleanField(default=False)
    comentario = models.CharField(max_length=100, null=True, blank=True)

    @property
    def total(self):
        return Decimal(self.monto_por_dia) * Decimal(self.cantidad_de_Dia)


    def __str__(self):
        return str(self.fecha_de_Renta)
    class Meta:
        verbose_name="Renta y Devolucion"
        verbose_name_plural="Rentas y Devoluciones"