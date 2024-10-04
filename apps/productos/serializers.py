from rest_framework import serializers
from .models import (Estatus, Categoria, EnfoqueTecnologia, LenguajeProgramacion,  Tecnologia,
                     SubDependencia, Dependencia, Solicitante, RolResponsable, Responsable,
                     ServidorWeb, TipoBaseDatos, BaseDatos, Producto, TecnologiaProducto,
                     ResponsableProducto, Infraestructura)


class EstatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estatus
        fields = '__all__'


class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = '__all__'


class EnfoqueTecnologiaSerializer(serializers.ModelSerializer):
    class Meta:
        model = EnfoqueTecnologia
        fields = '__all__'


class LenguajeProgramacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = LenguajeProgramacion
        fields = '__all__'


class TecnologiaSerializer(serializers.ModelSerializer):
    enfoque = EnfoqueTecnologiaSerializer()
    lenguaje = LenguajeProgramacionSerializer()

    class Meta:
        model = Tecnologia
        fields = '__all__'


class SubDependenciaSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubDependencia
        fields = '__all__'


class DependenciaSerializer(serializers.ModelSerializer):
    sub_dependencia = SubDependenciaSerializer()

    class Meta:
        model = Dependencia
        fields = '__all__'


class SolicitanteSerializer(serializers.ModelSerializer):
    dependencia = DependenciaSerializer()

    class Meta:
        model = Solicitante
        fields = '__all__'


class RolResponsableSerializer(serializers.ModelSerializer):
    class Meta:
        model = RolResponsable
        fields = '__all__'


class ResponsableSerializer(serializers.ModelSerializer):
    rol = RolResponsableSerializer()

    class Meta:
        model = Responsable
        fields = '__all__'


class ServidorWebSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServidorWeb
        fields = '__all__'


class TipoBaseDatosSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoBaseDatos
        fields = '__all__'


class BaseDatosSerializer(serializers.ModelSerializer):
    tipo = TipoBaseDatosSerializer()

    class Meta:
        model = BaseDatos
        fields = '__all__'


class ProductoSerializer(serializers.ModelSerializer):
    estatus = EstatusSerializer()
    categoria = CategoriaSerializer()
    tecnologias = serializers.SerializerMethodField()

    class Meta:
        model = Producto
        fields = '__all__'

    def get_tecnologias(self, obj):
        # Obtén todas las instancias de TecnologiaProducto relacionadas con el producto
        tecnologias_productos = TecnologiaProducto.objects.filter(producto=obj)
        # Serializa solo las tecnologías de cada TecnologiaProducto
        tecnologias = [tp.tecnologia for tp in tecnologias_productos]
        serializer = TecnologiaSerializer(tecnologias, many=True)
        return serializer.data

# Definicion de tablas intermedias


class TecnologiaProductoSerializer(serializers.ModelSerializer):
    producto = ProductoSerializer(read_only=True)
    producto_id = serializers.PrimaryKeyRelatedField(
        queryset=Producto.objects.all(), source='producto', write_only=True)
    tecnologia = TecnologiaSerializer(read_only=True)
    tecnologia_id = serializers.PrimaryKeyRelatedField(
        queryset=Tecnologia.objects.all(), source='tecnologia', write_only=True)

    class Meta:
        model = TecnologiaProducto
        fields = '__all__'


class ResponsableProductoSerializer(serializers.ModelSerializer):
    producto = ProductoSerializer(read_only=True)
    producto_id = serializers.PrimaryKeyRelatedField(
        queryset=Producto.objects.all(), source='producto', write_only=True)
    responsable = ResponsableSerializer(read_only=True)
    responsable_id = serializers.PrimaryKeyRelatedField(
        queryset=Responsable.objects.all(), source='responsable', write_only=True)

    class Meta:
        model = ResponsableProducto
        fields = '__all__'


class InfraestructuraSerializer(serializers.ModelSerializer):
    producto = ProductoSerializer(read_only=True)
    producto_id = serializers.PrimaryKeyRelatedField(
        queryset=Producto.objects.all(), source='producto', write_only=True)
    servidor_web = ServidorWebSerializer(read_only=True)
    servidor_web_id = serializers.PrimaryKeyRelatedField(
        queryset=ServidorWeb.objects.all(), source='servidor_web', write_only=True)
    base_datos = BaseDatosSerializer(read_only=True)
    base_datos_id = serializers.PrimaryKeyRelatedField(
        queryset=BaseDatos.objects.all(), source='base_datos', write_only=True)

    class Meta:
        model = Infraestructura
        fields = '__all__'
