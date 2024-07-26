from django.contrib import admin
from .models        import (Categoria, Tecnologia, Solicitante, Responsable, ServidorWeb, BaseDatos,
                            Version, Producto, TecnologiaProducto, ResponsableProducto, Infraestructura)

# Register your models here.

admin.site.register(Categoria)
admin.site.register(Tecnologia)
admin.site.register(Solicitante)
admin.site.register(Responsable)
admin.site.register(ServidorWeb)
admin.site.register(BaseDatos)
admin.site.register(Version)
admin.site.register(Producto)
admin.site.register(TecnologiaProducto)
admin.site.register(ResponsableProducto)
admin.site.register(Infraestructura)
