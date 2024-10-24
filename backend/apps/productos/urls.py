from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import (EstatusViewSet, CategoriaViewSet, EnfoqueTecnologiaViewSet, LenguajeProgramacionViewSet, TecnologiaViewSet,
                    SubDependenciaViewSet, DependenciaViewSet, SolicitanteViewSet, RolResponsableViewSet, ResponsableViewSet,ProductoViewSet, ProductoEstatusView, ProductoEstatusCountView, TecnologiaProductoViewSet, ResponsableProductoViewSet)

router = DefaultRouter()
router.register(r'estatus', EstatusViewSet)
router.register(r'categorias', CategoriaViewSet)
router.register(r'enfoques-tecnologia', EnfoqueTecnologiaViewSet)
router.register(r'lenguajes-programacion', LenguajeProgramacionViewSet)
router.register(r'tecnologias', TecnologiaViewSet)
router.register(r'sub-dependencias', SubDependenciaViewSet)
router.register(r'dependencias', DependenciaViewSet)
router.register(r'solicitantes', SolicitanteViewSet)
router.register(r'roles-responsables', RolResponsableViewSet)
router.register(r'responsables', ResponsableViewSet)
router.register(r'productos', ProductoViewSet)
router.register(r'tecnologias-productos', TecnologiaProductoViewSet)
router.register(r'responsables-productos', ResponsableProductoViewSet)

urlpatterns = router.urls + [
    path('producto-estatus/', ProductoEstatusView.as_view(),
         name='producto-estatus'),
    path('producto-estatus-count/', ProductoEstatusCountView.as_view(),
         name='producto-estatus-count'),
]