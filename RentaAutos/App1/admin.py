from django.contrib import admin
from django.template.defaultfilters import floatformat
from django.urls import reverse
from django.utils.html import format_html
from import_export import resources
from import_export.admin import ImportExportModelAdmin

from .models import TiposVehiculos, Marcas, TiposCombustible, Vehiculos, Clientes, Empleados, Inspeccion, Modelo, Renta_devolucion


#admin.site.register(TiposVehiculos)
@admin.register((TiposVehiculos))
class TiposVehiculosAdmin (admin.ModelAdmin):
    list_display = ('descripcion','estado')


class MarcasResource(resources.ModelResource):
    class Meta:
        model = Marcas

#admin.site.register(Marcas)
@admin.register((Marcas))
class MarcasAdmin (ImportExportModelAdmin):
    list_display = ('descripcion','estado')
    resource_class = Marcas

#admin.site.register(TiposCombustible)
@admin.register((TiposCombustible))
class TiposCombustibleAdmin (admin.ModelAdmin):
    list_display = ('descripcion','estado')


class VehiculoResource(resources.ModelResource):
    class Meta:
        Model = Vehiculos
#admin.site.register(Vehiculos)
@admin.register(Vehiculos)
class VehiculosAdmin (ImportExportModelAdmin):
    list_display = ('descripcion', 'chasis', 'motor', 'placa', 'tipo_de_vehiculo', 'marca', 'modelo', 'tipo_de_combustible', 'estado',)

class ClientesResource(resources.ModelResource):
    class Meta:
        Model = Clientes
#admin.site.register(Clientes)
@admin.register(Clientes)
class ClientesAdmin (ImportExportModelAdmin):
    search_fields = ('nombre', 'cedula')
    list_filter = ('tipo_de_persona',)
    list_display = ('nombre', 'cedula', 'tipo_de_persona')


class EmpleadosResource(resources.ModelResource):
        class Meta:
            Model = Empleados

#admin.site.register(Empleados)
@admin.register(Empleados)
class EmpleadosAdmin (ImportExportModelAdmin):
    list_display = ('nombre', 'cedula', 'tanda_labor', 'comision', 'fecha_de_ingreso', 'estado',)

class InspeccionResource(resources.ModelResource):
    class Meta:
        Model = Inspeccion

#admin.site.register(Inspeccion)
@admin.register(Inspeccion)
class InspeccionAdmin (ImportExportModelAdmin):
    list_display = ('vehiculo', 'ralladura', 'rotura_de_cristal', 'goma_de_repuesto', 'tiene_gato', 'cantidad_de_combustible', 'estado_de_gomas', 'fecha', 'estado',)

#admin.site.register(Modelo)
@admin.register(Modelo)
class ModeloAdmin (ImportExportModelAdmin):
    list_display = ('descripcion', 'estado', 'marca',)

class Renta_devolucionResource(resources.ModelResource):
    class Meta:
        Model = Renta_devolucion

#admin.site.register(Renta_devolucion)
@admin.register(Renta_devolucion)
class Renta_devolucionAdmin (ImportExportModelAdmin):
    list_display = ('numero_renta','empleado','vehiculo','fecha_de_Renta','fecha_de_Devuelta', 'format_total', 'devolver',
                    'cliente','estado','total')
    readonly_fields = ('numero_renta',)

    def format_total(self, obj):
        return floatformat(obj.total, 2)

    format_total.short_description = "total"

    def devolver(self, object):
        url_devolucion = reverse("devolver", kwargs={"id_renta": object.id})
        return format_html('<a class ="button" href="{}">Devolver</a>', url_devolucion)

admin.site.site_header= 'Classic RentaCar'
