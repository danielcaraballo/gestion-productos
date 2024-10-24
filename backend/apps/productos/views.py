from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import (Estatus, Categoria, EnfoqueTecnologia, LenguajeProgramacion, Tecnologia,
                     SubDependencia, Dependencia, Solicitante, RolResponsable, Responsable,
                     Producto,  TecnologiaProducto, ResponsableProducto)
from .serializers import (EstatusSerializer, CategoriaSerializer, EnfoqueTecnologiaSerializer, LenguajeProgramacionSerializer,
                          TecnologiaSerializer, SubDependenciaSerializer, DependenciaSerializer, SolicitanteSerializer, RolResponsableSerializer, ResponsableSerializer, ProductoSerializer, TecnologiaProductoSerializer, ResponsableProductoSerializer)


class EstatusViewSet(viewsets.ModelViewSet):
    queryset = Estatus.objects.all()
    serializer_class = EstatusSerializer


class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer


class EnfoqueTecnologiaViewSet(viewsets.ModelViewSet):
    queryset = EnfoqueTecnologia.objects.all()
    serializer_class = EnfoqueTecnologiaSerializer


class LenguajeProgramacionViewSet(viewsets.ModelViewSet):
    queryset = LenguajeProgramacion.objects.all()
    serializer_class = LenguajeProgramacionSerializer


class TecnologiaViewSet(viewsets.ModelViewSet):
    queryset = Tecnologia.objects.all()
    serializer_class = TecnologiaSerializer


class SubDependenciaViewSet(viewsets.ModelViewSet):
    queryset = SubDependencia.objects.all()
    serializer_class = SubDependenciaSerializer


class DependenciaViewSet(viewsets.ModelViewSet):
    queryset = Dependencia.objects.all()
    serializer_class = DependenciaSerializer


class SolicitanteViewSet(viewsets.ModelViewSet):
    queryset = Solicitante.objects.all()
    serializer_class = SolicitanteSerializer


class RolResponsableViewSet(viewsets.ModelViewSet):
    queryset = RolResponsable.objects.all()
    serializer_class = RolResponsableSerializer


class ResponsableViewSet(viewsets.ModelViewSet):
    queryset = Responsable.objects.all()
    serializer_class = ResponsableSerializer


class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer


class ProductoEstatusView(APIView):
    def get(self, request):
        estatus = Estatus.objects.all().values('id', 'nombre')
        return Response(estatus)


class ProductoEstatusCountView(APIView):
    def get(self, request):
        try:
            data = {
                "operativo": Producto.objects.filter(estatus__nombre="Operativo").count(),
                "mantenimiento": Producto.objects.filter(estatus__nombre="Mantenimiento").count(),
                "inactivo": Producto.objects.filter(estatus__nombre="Inactivo").count(),
                "retirado": Producto.objects.filter(estatus__nombre="Retirado").count(),
            }
            return Response(data)
        except Exception as e:
            return Response({"error": str(e)}, status=500)


# ViewSets para tablas intermedias


class TecnologiaProductoViewSet(viewsets.ModelViewSet):
    queryset = TecnologiaProducto.objects.all()
    serializer_class = TecnologiaProductoSerializer


class ResponsableProductoViewSet(viewsets.ModelViewSet):
    queryset = ResponsableProducto.objects.all()
    serializer_class = ResponsableProductoSerializer
