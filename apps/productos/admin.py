from django.contrib import admin
from .models import (Categoria, Tecnologia, Solicitante, Responsable, ServidorWeb, TipoBaseDatos, BaseDatos,
                     Version, Producto, TecnologiaProducto, ResponsableProducto, Infraestructura)

class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'descripcion', 'direccion_url', 'estatus', 'categoria')
    search_fields = ('nombre', 'descripcion')
    list_filter = ('estatus', 'categoria')

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
