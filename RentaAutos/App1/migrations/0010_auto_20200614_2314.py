# Generated by Django 3.0.7 on 2020-06-15 03:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App1', '0009_empleados_comision'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehiculos',
            name='motor',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='vehiculos',
            name='placa',
            field=models.CharField(max_length=50),
        ),
    ]
