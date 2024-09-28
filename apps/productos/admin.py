from django.contrib import admin
from .models import (Categoria, Tecnologia, Solicitante, Responsable, ServidorWeb, TipoBaseDatos, BaseDatos,
                     Version, Producto, TecnologiaProducto, ResponsableProducto, Infraestructura)


# Inline para manejar las tecnologías de un producto
class TecnologiaInline(admin.TabularInline):
    model = TecnologiaProducto  # Usar la tabla intermedia
    extra = 0  # Espacio adicional para añadir nuevas tecnologías


# Inline para manejar la infraestructura de un producto
class InfraestructuraInline(admin.TabularInline):
    model = Infraestructura  # Usar la tabla intermedia
    extra = False  # Espacio adicional


# Inline para manejar los responsables de un producto
class ResponsableInline(admin.TabularInline):
    model = ResponsableProducto
    extra = 0


class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'categoria', 'estatus', 'direccion_url')
    search_fields = ('nombre', 'descripcion')
    list_filter = ('estatus', 'categoria')
    inlines = [TecnologiaInline, InfraestructuraInline,
               ResponsableInline]  # Agregar inlines


class TecnologiaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'tipo', 'lenguaje', 'version')
    search_fields = ('nombre',)  # Agregar esto para la búsqueda en tecnologías


# Modelo Producto con la configuración personalizada
admin.site.register(Producto, ProductoAdmin)

# Register your models here.
admin.site.register(Categoria)
admin.site.register(Tecnologia)
admin.site.register(Solicitante)
admin.site.register(Responsable)
admin.site.register(ServidorWeb)
admin.site.register(TipoBaseDatos)
admin.site.register(BaseDatos)
admin.site.register(Version)
admin.site.register(TecnologiaProducto)
admin.site.register(ResponsableProducto)
admin.site.register(Infraestructura)
