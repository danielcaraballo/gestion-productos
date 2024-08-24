from rest_framework import serializers
from .models import (Categoria, Tecnologia, Solicitante, Responsable, ServidorWeb, TipoBaseDatos, BaseDatos,
                     Version, Producto, TecnologiaProducto, ResponsableProducto, Infraestructura)

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = '__all__'

class TecnologiaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tecnologia
        fields = '__all__'

class SolicitanteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Solicitante
        fields = '__all__'

class ResponsableSerializer(serializers.ModelSerializer):
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
    class Meta:
        model = BaseDatos
        fields = '__all__'

class VersionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Version
        fields = '__all__'

class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = '__all__'

# Definicion de tablas intermedias

class TecnologiaProductoSerializer(serializers.ModelSerializer):
    producto = ProductoSerializer(read_only=True)
    producto_id = serializers.PrimaryKeyRelatedField(queryset=Producto.objects.all(), source='producto', write_only=True)
    tecnologia = TecnologiaSerializer(read_only=True)
    tecnologia_id = serializers.PrimaryKeyRelatedField(queryset=Tecnologia.objects.all(), source='tecnologia', write_only=True)

    class Meta:
        model = TecnologiaProducto
        fields = '__all__'

class ResponsableProductoSerializer(serializers.ModelSerializer):
    producto = ProductoSerializer(read_only=True)
    producto_id = serializers.PrimaryKeyRelatedField(queryset=Producto.objects.all(), source='producto', write_only=True)
    responsable = ResponsableSerializer(read_only=True)
    responsable_id = serializers.PrimaryKeyRelatedField(queryset=Responsable.objects.all(), source='responsable', write_only=True) 
    
    class Meta:
        model = ResponsableProducto
        fields = '__all__'

class InfraestructuraSerializer(serializers.ModelSerializer):
    producto = ProductoSerializer(read_only=True)
    producto_id = serializers.PrimaryKeyRelatedField(queryset=Producto.objects.all(), source='producto', write_only=True)
    servidor_web = ServidorWebSerializer(read_only=True)
    servidor_web_id = serializers.PrimaryKeyRelatedField(queryset=ServidorWeb.objects.all(), source='servidor_web', write_only=True)
    base_datos = BaseDatosSerializer(read_only=True)
    base_datos_id = serializers.PrimaryKeyRelatedField(queryset=BaseDatos.objects.all(), source='base_datos', write_only=True)
    
    class Meta:
        model = Infraestructura
        fields = '__all__'
