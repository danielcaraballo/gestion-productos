from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import (Categoria, Tecnologia, Solicitante, Responsable, ServidorWeb, TipoBaseDatos, BaseDatos, Version,
                     Producto,  TecnologiaProducto, ResponsableProducto, Infraestructura)
from .serializers import (CategoriaSerializer, TecnologiaSerializer, SolicitanteSerializer, ResponsableSerializer,
                          ServidorWebSerializer, TipoBaseDatosSerializer, BaseDatosSerializer, VersionSerializer,
                          ProductoSerializer, TecnologiaProductoSerializer, ResponsableProductoSerializer, InfraestructuraSerializer)

# Create your views here. ViewSets para los modelos


class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer


class TecnologiaViewSet(viewsets.ModelViewSet):
    queryset = Tecnologia.objects.all()
    serializer_class = TecnologiaSerializer


class SolicitanteViewSet(viewsets.ModelViewSet):
    queryset = Solicitante.objects.all()
    serializer_class = SolicitanteSerializer


class ResponsableViewSet(viewsets.ModelViewSet):
    queryset = Responsable.objects.all()
    serializer_class = ResponsableSerializer


class ServidorWebViewSet(viewsets.ModelViewSet):
    queryset = ServidorWeb.objects.all()
    serializer_class = ServidorWebSerializer


class TipoBaseDatosViewSet(viewsets.ModelViewSet):
    queryset = TipoBaseDatos.objects.all()
    serializer_class = TipoBaseDatosSerializer


class BaseDatosViewSet(viewsets.ModelViewSet):
    queryset = BaseDatos.objects.all()
    serializer_class = BaseDatosSerializer


class VersionViewSet(viewsets.ModelViewSet):
    queryset = Version.objects.all()
    serializer_class = VersionSerializer


class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer


class ProductoEstatusCountView(APIView):
    def get(self, request):
        data = {
            "operativo": Producto.objects.filter(estatus="Operativo").count(),
            "mantenimiento": Producto.objects.filter(estatus="Mantenimiento").count(),
            "inactivo": Producto.objects.filter(estatus="Inactivo").count(),
            "retirado": Producto.objects.filter(estatus="Retirado").count(),
        }
        return Response(data)

# ViewSets para tablas intermedias


class TecnologiaProductoViewSet(viewsets.ModelViewSet):
    queryset = TecnologiaProducto.objects.all()
    serializer_class = TecnologiaProductoSerializer


class ResponsableProductoViewSet(viewsets.ModelViewSet):
    queryset = ResponsableProducto.objects.all()
    serializer_class = ResponsableProductoSerializer


class InfraestructuraViewSet(viewsets.ModelViewSet):
    queryset = Infraestructura.objects.all()
    serializer_class = InfraestructuraSerializer
