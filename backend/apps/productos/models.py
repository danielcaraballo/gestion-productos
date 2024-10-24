from django.db import models


class Estatus(models.Model):
    nombre = models.CharField(
        max_length=50, verbose_name="Nombre del Estatus")

    def __str__(self) -> str:
        return self.nombre

    class Meta:
        verbose_name = "Estatus"
        verbose_name_plural = "Estatus"


class Categoria(models.Model):
    nombre = models.CharField(
        max_length=100, verbose_name="Nombre de la Categoria")

    def __str__(self) -> str:
        return self.nombre

    class Meta:
        verbose_name = "Categoría"
        verbose_name_plural = "Categorías"


class EnfoqueTecnologia(models.Model):
    nombre = models.CharField(max_length=50, verbose_name="Nombre del Enfoque")

    def __str__(self) -> str:
        return self.nombre

    class Meta:
        verbose_name = "Enfoque de la Tecnologia"
        verbose_name_plural = "Enfoque de las Tecnologias"


class LenguajeProgramacion(models.Model):
    nombre = models.CharField(
        max_length=50, verbose_name="Nombre del Lenguaje")

    def __str__(self) -> str:
        return self.nombre

    class Meta:
        verbose_name = "Lenguaje de Programacion"
        verbose_name_plural = "Lenguajes de Programacion"


class Tecnologia(models.Model):
    nombre = models.CharField(
        max_length=100, verbose_name="Nombre de la Tecnologia")
    enfoque = models.ForeignKey(EnfoqueTecnologia, on_delete=models.PROTECT)
    lenguaje = models.ForeignKey(
        LenguajeProgramacion, on_delete=models.PROTECT)

    def __str__(self) -> str:
        return f"{self.nombre} ({self.enfoque})"

    class Meta:
        verbose_name = "Tecnologia"
        verbose_name_plural = "Tecnologias"


class Dependencia(models.Model):
    nombre = models.CharField(
        max_length=100, verbose_name="Nombre de la Dependencia")

    def __str__(self) -> str:
        return self.nombre

    class Meta:
        verbose_name = "Dependencia"
        verbose_name_plural = "Dependencias"


class SubDependencia(models.Model):
    nombre = models.CharField(
        max_length=100, verbose_name="Nombre de la SubDependencia")
    dependencia = models.ForeignKey(
        Dependencia, on_delete=models.CASCADE, related_name='sub_dependencias')

    def __str__(self) -> str:
        return self.nombre

    class Meta:
        verbose_name = "SubDependencia"
        verbose_name_plural = "SubDependencias"


class Solicitante(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    cargo = models.CharField(max_length=100)
    contacto = models.CharField(max_length=100)
    dependencia = models.ForeignKey(
        Dependencia, on_delete=models.PROTECT, related_name='solicitantes')
    sub_dependencia = models.ForeignKey(
        SubDependencia, on_delete=models.PROTECT, null=True, blank=True)

    def __str__(self) -> str:
        return f"{self.nombre} {self.apellido} - {self.dependencia}"

    class Meta:
        verbose_name = "Solicitante"
        verbose_name_plural = "Solicitantes"


class RolResponsable(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.nombre

    class Meta:
        verbose_name = "Rol de Responsable"
        verbose_name_plural = "Roles de Responsables"


class Responsable(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    contacto = models.CharField(max_length=50)
    rol = models.ForeignKey(RolResponsable, on_delete=models.PROTECT)

    def __str__(self) -> str:
        return f"{self.nombre} {self.apellido} ({self.rol})"

    class Meta:
        verbose_name = "Responsable"
        verbose_name_plural = "Responsables"


class Producto(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField()
    direccion_url = models.URLField()
    fecha_lanzamiento = models.DateField()
    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT)
    solicitante = models.ForeignKey(Solicitante, on_delete=models.PROTECT)
    estatus = models.ForeignKey(Estatus, on_delete=models.PROTECT)

    def __str__(self) -> str:
        return self.nombre

    class Meta:
        verbose_name = "Producto"
        verbose_name_plural = "Productos"


# Definicion de tablas intermedias


class TecnologiaProducto(models.Model):
    tecnologia = models.ForeignKey(Tecnologia, on_delete=models.PROTECT)
    producto = models.ForeignKey(Producto, on_delete=models.PROTECT)

    def __str__(self) -> str:
        return f"{self.producto.nombre} - {self.tecnologia.nombre}"

    class Meta:
        verbose_name = "Tecnologia del Producto"
        verbose_name_plural = "Tecnologias de los Productos"


class ResponsableProducto(models.Model):
    responsable = models.ForeignKey(Responsable, on_delete=models.PROTECT)
    producto = models.ForeignKey(Producto, on_delete=models.PROTECT)

    def __str__(self) -> str:
        return f"{self.producto.nombre} - {self.responsable.nombre}"

    class Meta:
        verbose_name = "Responsable del Producto"
        verbose_name_plural = "Responsables de los Productos"
