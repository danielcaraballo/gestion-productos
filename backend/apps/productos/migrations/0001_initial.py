# Generated by Django 5.1 on 2024-10-04 01:54

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BaseDatos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('direccion_ip', models.GenericIPAddressField()),
            ],
            options={
                'verbose_name': 'Base de Datos',
                'verbose_name_plural': 'Bases de Datos',
            },
        ),
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100, verbose_name='Nombre de la Categoria')),
            ],
            options={
                'verbose_name': 'Categoría',
                'verbose_name_plural': 'Categorías',
            },
        ),
        migrations.CreateModel(
            name='Dependencia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100, verbose_name='Nombre de la Dependencia')),
            ],
            options={
                'verbose_name': 'Dependencia',
                'verbose_name_plural': 'Dependencias',
            },
        ),
        migrations.CreateModel(
            name='EnfoqueTecnologia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50, verbose_name='Nombre del Enfoque')),
            ],
            options={
                'verbose_name': 'Enfoque de la Tecnologia',
                'verbose_name_plural': 'Enfoque de las Tecnologias',
            },
        ),
        migrations.CreateModel(
            name='Estatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50, verbose_name='Nombre del Estatus')),
            ],
            options={
                'verbose_name': 'Estatus',
                'verbose_name_plural': 'Estatus',
            },
        ),
        migrations.CreateModel(
            name='LenguajeProgramacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50, verbose_name='Nombre del Lenguaje')),
            ],
            options={
                'verbose_name': 'Lenguaje de Programacion',
                'verbose_name_plural': 'Lenguajes de Programacion',
            },
        ),
        migrations.CreateModel(
            name='Responsable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('apellido', models.CharField(max_length=100)),
                ('contacto', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'Responsable',
                'verbose_name_plural': 'Responsables',
            },
        ),
        migrations.CreateModel(
            name='RolResponsable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Rol de Responsable',
                'verbose_name_plural': 'Roles de Responsables',
            },
        ),
        migrations.CreateModel(
            name='SubDependencia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100, verbose_name='Nombre de la Sub Dependencia')),
            ],
            options={
                'verbose_name': 'Sub Dependencia',
                'verbose_name_plural': 'Sub Dependencias',
            },
        ),
        migrations.CreateModel(
            name='TipoBaseDatos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Tipo de Base de Datos',
                'verbose_name_plural': 'Tipos de Bases de Datos',
            },
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('descripcion', models.TextField()),
                ('direccion_url', models.URLField()),
                ('fecha_lanzamiento', models.DateField()),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='productos.categoria')),
                ('estatus', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='productos.estatus')),
            ],
            options={
                'verbose_name': 'Producto',
                'verbose_name_plural': 'Productos',
            },
        ),
        migrations.CreateModel(
            name='ResponsableProducto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='productos.producto')),
                ('responsable', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='productos.responsable')),
            ],
            options={
                'verbose_name': 'Responsable del Producto',
                'verbose_name_plural': 'Responsables de los Productos',
            },
        ),
        migrations.AddField(
            model_name='responsable',
            name='rol',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='productos.rolresponsable'),
        ),
        migrations.CreateModel(
            name='ServidorWeb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('direccion_ip', models.GenericIPAddressField()),
                ('estatus', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='productos.estatus')),
            ],
            options={
                'verbose_name': 'Servidor Web',
                'verbose_name_plural': 'Servidores Web',
            },
        ),
        migrations.CreateModel(
            name='Infraestructura',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('base_datos', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='productos.basedatos')),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='productos.producto')),
                ('servidor_web', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='productos.servidorweb')),
            ],
            options={
                'verbose_name': 'Infraestructura del Producto',
                'verbose_name_plural': 'Infraestructuras de los Productos',
            },
        ),
        migrations.CreateModel(
            name='Solicitante',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('apellido', models.CharField(max_length=50)),
                ('cargo', models.CharField(max_length=100)),
                ('contacto', models.CharField(max_length=100)),
                ('dependencia', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='productos.dependencia')),
            ],
            options={
                'verbose_name': 'Solicitante',
                'verbose_name_plural': 'Solicitantes',
            },
        ),
        migrations.AddField(
            model_name='producto',
            name='solicitante',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='productos.solicitante'),
        ),
        migrations.AddField(
            model_name='dependencia',
            name='sub_dependencia',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='productos.subdependencia'),
        ),
        migrations.CreateModel(
            name='Tecnologia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100, verbose_name='Nombre de la Tecnologia')),
                ('enfoque', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='productos.enfoquetecnologia')),
                ('lenguaje', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='productos.lenguajeprogramacion')),
            ],
            options={
                'verbose_name': 'Tecnologia',
                'verbose_name_plural': 'Tecnologias',
            },
        ),
        migrations.CreateModel(
            name='TecnologiaProducto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='productos.producto')),
                ('tecnologia', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='productos.tecnologia')),
            ],
            options={
                'verbose_name': 'Tecnologia del Producto',
                'verbose_name_plural': 'Tecnologias de los Productos',
            },
        ),
        migrations.AddField(
            model_name='basedatos',
            name='tipo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='basesdatos', to='productos.tipobasedatos'),
        ),
    ]