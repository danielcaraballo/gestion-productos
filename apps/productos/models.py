from django.db import models

# Opciones de Estatus

ESTATUS_CHOICES = [
        ('Operativo', 'Operativo'),
        ('Mantenimiento', 'Mantenimiento'),
        ('Inactivo', 'Inactivo'),
        ('Retirado', 'Retirado'),
    ]

# Definicion de Entidades

class Categoria(models.Model):
    nombre = models.CharField(max_length=100, verbose_name="Nombre de la Categoria")
    descripcion = models.TextField(verbose_name="Descripcion de la Categoria")

    def __str__(self) -> str:
        return self.nombre

    class Meta:
        verbose_name = "Categoría"
        verbose_name_plural = "Categorías"

class Tecnologia(models.Model):
    TIPO_CHOICES = [
        ('Base de datos', 'Base de datos'),
        ('Backend', 'Backend'),
        ('Frontend', 'Frontend')
    ]
    nombre = models.CharField(max_length=100, verbose_name="Nombre de la Tecnologia")
    tipo = models.CharField(max_length=100, choices=TIPO_CHOICES, verbose_name="Tipo")
    lenguaje = models.CharField(max_length=100, verbose_name="Lenguaje")
    version = models.CharField(max_length=50, verbose_name="Version de la Tecnologia")

    def __str__(self) -> str:
        return f"{self.nombre} v{self.version} ({self.tipo})"
    
    class Meta:
        verbose_name = "Tecnologia"
        verbose_name_plural = "Tecnologias"
    
class Solicitante(models.Model):
    origen = models.CharField(max_length=50)
    cedula = models.CharField(max_length=50, unique=True)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    cargo = models.CharField(max_length=100)
    dependencia = models.CharField(max_length=100)
    contacto = models.CharField(max_length=100)

    def __str__(self) -> str:
        return f"{self.nombre} {self.apellido}"
    
    class Meta:
        verbose_name = "Solicitante"
        verbose_name_plural = "Solicitantes"

class Responsable(models.Model):
    ROL_CHOICES = [
        ('Gestor de proyecto', 'Gestor del proyecto'),
        ('Analista de requerimientos', 'Analista de requerimientos')
        ('Programador', 'Programador'),
    ]
    origen = models.CharField(max_length=50)
    cedula = models.CharField(max_length=50, unique=True)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    rol = models.CharField(max_length=100, choices=ROL_CHOICES)
    contacto = models.CharField(max_length=50)

    def __str__(self) -> str:
        return f"{self.nombre} {self.apellido} ({self.rol})"
    
    class Meta:
        verbose_name = "Responsable"
        verbose_name_plural = "Responsables"
    
class ServidorWeb(models.Model):
    direccion_ip = models.GenericIPAddressField()
    estatus = models.CharField(max_length=50, choices=ESTATUS_CHOICES)

    def __str__(self) -> str:
        return f"{self.direccion_ip} ({self.estatus})"
    
    class Meta:
        verbose_name = "Servidor Web"
        verbose_name_plural = "Servidores Web"
    
class BaseDatos(models.Model):
    direccion_ip = models.GenericIPAddressField()
    nombre = models.CharField(max_length=100)
    tipo = models.CharField(max_length=50)

    def __str__(self) -> str:
        return f"{self.nombre} ({self.direccion_ip})"
    
    class Meta:
        verbose_name = "Base de Datos"
        verbose_name_plural = "Bases de Datos"
    
class Version(models.Model):
    numero = models.CharField(max_length=50)
    fecha_lanzamiento = models.DateField()
    nota = models.TextField()

    def __str__(self) -> str:
        return self.numero
    
    class Meta:
        verbose_name = "Version"
        verbose_name_plural = "Versiones"
    
class Producto(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField()
    direccion_url = models.URLField()
    estatus = models.CharField(max_length=100, choices=ESTATUS_CHOICES)
    fecha_lanzamiento = models.DateField()
    version = models.ForeignKey(Version, on_delete=models.PROTECT) 
    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT)
    solicitante = models.ForeignKey(Solicitante, on_delete=models.PROTECT)

    def __str__(self) -> str:
        return self.nombre
    
    class Meta:
        verbose_name = "Producto"
        verbose_name_plural = "Productos"

# Definicion de tablas intermedias

class TecnologiaProducto(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.PROTECT)
    tecnologia = models.ForeignKey(Tecnologia, on_delete=models.PROTECT)

    def __str__(self) -> str:
        return f"{self.producto.nombre} - {self.tecnologia.nombre}"
    
    class Meta:
        verbose_name = "Tecnologia del Producto"
        verbose_name_plural = "Tecnologias de los Productos"
    
class ResponsableProducto(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.PROTECT)
    responsable = models.ForeignKey(Responsable, on_delete=models.PROTECT)

    def __str__(self) -> str:
        return f"{self.producto.nombre} - {self.responsable.nombre}"
    
    class Meta:
        verbose_name = "Responsable del Producto"
        verbose_name_plural = "Responsables de los Productos"
    
class Infraestructura(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.PROTECT)
    servidor_web = models.ForeignKey(ServidorWeb, on_delete=models.PROTECT)
    base_datos = models.ForeignKey(BaseDatos, on_delete=models.PROTECT)

    def __str__(self):
        return f"{self.producto.nombre} - {self.servidor_web.direccion_ip} - {self.base_datos.nombre}"
    
    class Meta:
        verbose_name = "Infraestructura del Producto"
        verbose_name_plural = "Infraestructuras de los Productos"
