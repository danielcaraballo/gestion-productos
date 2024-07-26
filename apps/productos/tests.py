from django.test    import TestCase
from .models        import (Categoria, Tecnologia, Solicitante, Responsable, ServidorWeb, BaseDatos,
                            Version, Producto, TecnologiaProducto, ResponsableProducto, Infraestructura)

class CategoriaModelTest(TestCase):
    def setUp(self):
        self.categoria = Categoria.objects.create(
            nombre="Categoria1",
            descripcion="Descripción de la categoría"
        )

    def test_categoria_str(self):
        self.assertEqual(str(self.categoria), "Categoria1")

    def test_categoria_fields(self):
        self.assertEqual(self.categoria.nombre, "Categoria1")
        self.assertEqual(self.categoria.descripcion, "Descripción de la categoría")


class TecnologiaModelTest(TestCase):
    def setUp(self):
        self.tecnologia = Tecnologia.objects.create(
            nombre="Tecnologia1",
            tipo="Backend",
            lenguaje="Python",
            version="1.0"
        )

    def test_tecnologia_str(self):
        self.assertEqual(str(self.tecnologia), "Tecnologia1 v1.0 (Backend)")

    def test_tecnologia_fields(self):
        self.assertEqual(self.tecnologia.nombre, "Tecnologia1")
        self.assertEqual(self.tecnologia.tipo, "Backend")
        self.assertEqual(self.tecnologia.lenguaje, "Python")
        self.assertEqual(self.tecnologia.version, "1.0")


class SolicitanteModelTest(TestCase):
    def setUp(self):
        self.solicitante = Solicitante.objects.create(
            origen="Interno",
            cedula="123456789",
            nombre="Nombre",
            apellido="Apellido",
            cargo="Cargo",
            dependencia="Dependencia",
            contacto="Contacto"
        )

    def test_solicitante_str(self):
        self.assertEqual(str(self.solicitante), "Nombre Apellido")

    def test_solicitante_fields(self):
        self.assertEqual(self.solicitante.origen, "Interno")
        self.assertEqual(self.solicitante.cedula, "123456789")
        self.assertEqual(self.solicitante.nombre, "Nombre")
        self.assertEqual(self.solicitante.apellido, "Apellido")
        self.assertEqual(self.solicitante.cargo, "Cargo")
        self.assertEqual(self.solicitante.dependencia, "Dependencia")
        self.assertEqual(self.solicitante.contacto, "Contacto")


class ResponsableModelTest(TestCase):
    def setUp(self):
        self.responsable = Responsable.objects.create(
            origen="Interno",
            cedula="987654321",
            nombre="NombreResp",
            apellido="ApellidoResp",
            rol="Programador",
            contacto="ContactoResp"
        )

    def test_responsable_str(self):
        self.assertEqual(str(self.responsable), "NombreResp ApellidoResp (Programador)")

    def test_responsable_fields(self):
        self.assertEqual(self.responsable.origen, "Interno")
        self.assertEqual(self.responsable.cedula, "987654321")
        self.assertEqual(self.responsable.nombre, "NombreResp")
        self.assertEqual(self.responsable.apellido, "ApellidoResp")
        self.assertEqual(self.responsable.rol, "Programador")
        self.assertEqual(self.responsable.contacto, "ContactoResp")


class ServidorWebModelTest(TestCase):
    def setUp(self):
        self.servidor_web = ServidorWeb.objects.create(
            direccion_ip="192.168.1.1",
            estatus="Operativo"
        )

    def test_servidor_web_str(self):
        self.assertEqual(str(self.servidor_web), "192.168.1.1 (Operativo)")

    def test_servidor_web_fields(self):
        self.assertEqual(self.servidor_web.direccion_ip, "192.168.1.1")
        self.assertEqual(self.servidor_web.estatus, "Operativo")


class BaseDatosModelTest(TestCase):
    def setUp(self):
        self.base_datos = BaseDatos.objects.create(
            direccion_ip="192.168.1.2",
            nombre="BaseDatos1",
            tipo="PostgreSQL"
        )

    def test_base_datos_str(self):
        self.assertEqual(str(self.base_datos), "BaseDatos1 (192.168.1.2)")

    def test_base_datos_fields(self):
        self.assertEqual(self.base_datos.direccion_ip, "192.168.1.2")
        self.assertEqual(self.base_datos.nombre, "BaseDatos1")
        self.assertEqual(self.base_datos.tipo, "PostgreSQL")


class VersionModelTest(TestCase):
    def setUp(self):
        self.version = Version.objects.create(
            numero="1.0.0",
            fecha_lanzamiento="2024-01-01",
            nota="Notas de la versión"
        )

    def test_version_str(self):
        self.assertEqual(str(self.version), "1.0.0")

    def test_version_fields(self):
        self.assertEqual(self.version.numero, "1.0.0")
        self.assertEqual(self.version.fecha_lanzamiento, "2024-01-01")
        self.assertEqual(self.version.nota, "Notas de la versión")


class ProductoModelTest(TestCase):
    def setUp(self):
        self.version = Version.objects.create(
            numero="1.0.0",
            fecha_lanzamiento="2024-01-01",
            nota="Notas de la versión"
        )
        self.categoria = Categoria.objects.create(
            nombre="Categoria1",
            descripcion="Descripción de la categoría"
        )
        self.solicitante = Solicitante.objects.create(
            origen="Interno",
            cedula="123456789",
            nombre="Nombre",
            apellido="Apellido",
            cargo="Cargo",
            dependencia="Dependencia",
            contacto="Contacto"
        )
        self.producto = Producto.objects.create(
            nombre="Producto1",
            descripcion="Descripción del producto",
            direccion_url="http://example.com",
            estatus="Operativo",
            fecha_lanzamiento="2024-01-01",
            version=self.version,
            categoria=self.categoria,
            solicitante=self.solicitante
        )

    def test_producto_str(self):
        self.assertEqual(str(self.producto), "Producto1")

    def test_producto_fields(self):
        self.assertEqual(self.producto.nombre, "Producto1")
        self.assertEqual(self.producto.descripcion, "Descripción del producto")
        self.assertEqual(self.producto.direccion_url, "http://example.com")
        self.assertEqual(self.producto.estatus, "Operativo")
        self.assertEqual(self.producto.fecha_lanzamiento, "2024-01-01")
        self.assertEqual(self.producto.version, self.version)
        self.assertEqual(self.producto.categoria, self.categoria)
        self.assertEqual(self.producto.solicitante, self.solicitante)


class TecnologiaProductoModelTest(TestCase):
    def setUp(self):
        self.producto = Producto.objects.create(
            nombre="Producto1",
            descripcion="Descripción del producto",
            direccion_url="http://example.com",
            estatus="Operativo",
            fecha_lanzamiento="2024-01-01",
            version=Version.objects.create(
                numero="1.0.0",
                fecha_lanzamiento="2024-01-01",
                nota="Notas de la versión"
            ),
            categoria=Categoria.objects.create(
                nombre="Categoria1",
                descripcion="Descripción de la categoría"
            ),
            solicitante=Solicitante.objects.create(
                origen="Interno",
                cedula="123456789",
                nombre="Nombre",
                apellido="Apellido",
                cargo="Cargo",
                dependencia="Dependencia",
                contacto="Contacto"
            )
        )
        self.tecnologia = Tecnologia.objects.create(
            nombre="Tecnologia1",
            tipo="Backend",
            lenguaje="Python",
            version="1.0"
        )
        self.tecnologia_producto = TecnologiaProducto.objects.create(
            producto=self.producto,
            tecnologia=self.tecnologia
        )

    def test_tecnologia_producto_str(self):
        self.assertEqual(str(self.tecnologia_producto), "Producto1 - Tecnologia1")

    def test_tecnologia_producto_fields(self):
        self.assertEqual(self.tecnologia_producto.producto, self.producto)
        self.assertEqual(self.tecnologia_producto.tecnologia, self.tecnologia)


class ResponsableProductoModelTest(TestCase):
    def setUp(self):
        self.producto = Producto.objects.create(
            nombre="Producto1",
            descripcion="Descripción del producto",
            direccion_url="http://example.com",
            estatus="Operativo",
            fecha_lanzamiento="2024-01-01",
            version=Version.objects.create(
                numero="1.0.0",
                fecha_lanzamiento="2024-01-01",
                nota="Notas de la versión"
            ),
            categoria=Categoria.objects.create(
                nombre="Categoria1",
                descripcion="Descripción de la categoría"
            ),
            solicitante=Solicitante.objects.create(
                origen="Interno",
                cedula="123456789",
                nombre="Nombre",
                apellido="Apellido",
                cargo="Cargo",
                dependencia="Dependencia",
                contacto="Contacto"
            )
        )
        self.responsable = Responsable.objects.create(
            origen="Interno",
            cedula="987654321",
            nombre="NombreResp",
            apellido="ApellidoResp",
            rol="Programador",
            contacto="ContactoResp"
        )
        self.responsable_producto = ResponsableProducto.objects.create(
            producto=self.producto,
            responsable=self.responsable
        )

    def test_responsable_producto_str(self):
        self.assertEqual(str(self.responsable_producto), "Producto1 - NombreResp")

    def test_responsable_producto_fields(self):
        self.assertEqual(self.responsable_producto.producto, self.producto)
        self.assertEqual(self.responsable_producto.responsable, self.responsable)


class InfraestructuraModelTest(TestCase):
    def setUp(self):
        self.producto = Producto.objects.create(
            nombre="Producto1",
            descripcion="Descripción del producto",
            direccion_url="http://example.com",
            estatus="Operativo",
            fecha_lanzamiento="2024-01-01",
            version=Version.objects.create(
                numero="1.0.0",
                fecha_lanzamiento="2024-01-01",
                nota="Notas de la versión"
            ),
            categoria=Categoria.objects.create(
                nombre="Categoria1",
                descripcion="Descripción de la categoría"
            ),
            solicitante=Solicitante.objects.create(
                origen="Interno",
                cedula="123456789",
                nombre="Nombre",
                apellido="Apellido",
                cargo="Cargo",
                dependencia="Dependencia",
                contacto="Contacto"
            )
        )
        self.servidor_web = ServidorWeb.objects.create(
            direccion_ip="192.168.1.1",
            estatus="Operativo"
        )
        self.base_datos = BaseDatos.objects.create(
            direccion_ip="192.168.1.2",
            nombre="BaseDatos1",
            tipo="PostgreSQL"
        )
        self.infraestructura = Infraestructura.objects.create(
            producto=self.producto,
            servidor_web=self.servidor_web,
            base_datos=self.base_datos
        )

    def test_infraestructura_str(self):
        self.assertEqual(str(self.infraestructura), "Producto1 - 192.168.1.1 - BaseDatos1")

    def test_infraestructura_fields(self):
        self.assertEqual(self.infraestructura.producto, self.producto)
        self.assertEqual(self.infraestructura.servidor_web, self.servidor_web)
        self.assertEqual(self.infraestructura.base_datos, self.base_datos)
