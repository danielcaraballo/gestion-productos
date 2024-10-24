# Generated by Django 5.1 on 2024-10-13 23:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0004_remove_dependencia_sub_dependencia_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='basedatos',
            name='tipo',
        ),
        migrations.RemoveField(
            model_name='infraestructura',
            name='base_datos',
        ),
        migrations.RemoveField(
            model_name='infraestructura',
            name='producto',
        ),
        migrations.RemoveField(
            model_name='infraestructura',
            name='servidor_web',
        ),
        migrations.RemoveField(
            model_name='servidorweb',
            name='estatus',
        ),
        migrations.DeleteModel(
            name='TipoBaseDatos',
        ),
        migrations.DeleteModel(
            name='BaseDatos',
        ),
        migrations.DeleteModel(
            name='Infraestructura',
        ),
        migrations.DeleteModel(
            name='ServidorWeb',
        ),
    ]