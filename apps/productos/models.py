from django.db import models

# Definicion de Estatus

ESTATUS_CHOICES = [
        ('Operativo', 'Operativo'),
        ('Mantenimiento', 'Mantenimiento'),
        ('Inactivo', 'Inactivo'),
        ('Retirado', 'Retirado'),
    ]

# Definicion de Entidades

class Categoria(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()

    def __str__(self) -> str:
        return self.nombre

class Tecnologia(models.Model):
    TIPO_CHOICES = [
        ('Base de datos', 'Base de datos'),
        ('Backend', 'Backend'),
        ('Frontend', 'Frontend')
    ]
    nombre = models.CharField(max_length=100)
    tipo = models.CharField(max_length=100, choices=TIPO_CHOICES)
    lenguaje = models.CharField(max_length=100)
    version = models.CharField(max_length=50)

    def __str__(self) -> str:
        return f"{self.nombre} v{self.version} ({self.tipo})"
    
class Solicitante(models.Model):
    origen = models.CharField(max_length=50)
    cedula = models.CharField(max_length=50)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    cargo = models.CharField(max_length=100)
    dependencia = models.CharField(max_length=100)
    contacto = models.CharField(max_length=100)

    def __str__(self) -> str:
        return f"{self.nombre} {self.apellido}"

class Responsable(models.Model):
    ROL_CHOICES = [
        ('Gestor del Proyecto', 'Gestor del Proyecto'),
        ('Analista de Requerimientos', 'Analista de Requerimientos')
        ('Programador', 'Programador'),
    ]
    origen = models.CharField(max_length=50)
    cedula = models.CharField(max_length=50)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    rol = models.CharField(max_length=100, choices=ROL_CHOICES)
    contacto = models.CharField(max_length=50)

    def __str__(self) -> str:
        return f"{self.nombre} {self.apellido} ({self.rol})"
    
class ServidorWeb(models.Model):
    direccion_ip = models.GenericIPAddressField()
    estatus = models.CharField(max_length=50, choices=ESTATUS_CHOICES)

    def __str__(self) -> str:
        return f"{self.direccion_ip} ({self.estatus})"
    
class BaseDeDatos(models.Model):
    direccion_ip = models.GenericIPAddressField()
    nombre = models.CharField(max_length=100)
    tipo = models.CharField(max_length=50)

    def __str__(self) -> str:
        return f"{self.nombre} ({self.direccion_ip})"
    
class Version(models.Model):
    numero = models.CharField(max_length=50)
    fecha_lanzamiento = models.DateField()
    nota = models.TextField()

    def __str__(self) -> str:
        return self.numero
    
class Producto(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField()
    direccion_url = models.URLField()
    estatus = models.CharField(max_length=100, choices=ESTATUS_CHOICES)
    fecha_lanzamiento = models.DateField()
    version = models.ForeignKey(Version, on_delete=models.CASCADE) 
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    solicitante = models.models.ForeignKey(Solicitante, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.nombre

# Definicion de tablas intermedias

class TecnologiaProducto(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    tecnologia = models.ForeignKey(Tecnologia, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.producto} - {self.tecnologia}"
    
class ResponsableProducto(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    responsable = models.ForeignKey(Responsable, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.producto} - {self.responsable}"
    
class Infraestructura(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    servidor_web = models.ForeignKey(ServidorWeb, on_delete=models.CASCADE)
    base_de_datos = models.ForeignKey(BaseDeDatos, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.producto} - {self.servidor_web} - {self.base_de_datos}"
