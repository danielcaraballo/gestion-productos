from rest_framework.routers import DefaultRouter
from .views import (CategoriaViewSet, TecnologiaViewSet, SolicitanteViewSet, ResponsableViewSet,
                    ServidorWebViewSet, TipoBaseDatosViewSet, BaseDatosViewSet, VersionViewSet,
                    ProductoViewSet, TecnologiaProductoViewSet, ResponsableProductoViewSet,
                    InfraestructuraViewSet)

router = DefaultRouter()
router.register(r'categorias', CategoriaViewSet)
router.register(r'tecnologias', TecnologiaViewSet)
router.register(r'solicitantes', SolicitanteViewSet)
router.register(r'responsables', ResponsableViewSet)
router.register(r'servidores-web', ServidorWebViewSet)
router.register(r'tipos-bases-datos', TipoBaseDatosViewSet)
router.register(r'bases-datos', BaseDatosViewSet)
router.register(r'versiones', VersionViewSet)
router.register(r'productos', ProductoViewSet)
router.register(r'tecnologias-productos', TecnologiaProductoViewSet)
router.register(r'responsables-productos', ResponsableProductoViewSet)
router.register(r'infraestructuras', InfraestructuraViewSet)

urlpatterns = router.urls
