# Generated by Django 3.0.7 on 2020-06-09 00:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('App1', '0006_auto_20200608_2031'),
    ]

    operations = [
        migrations.CreateModel(
            name='Renta_devolucion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_de_Renta', models.DateTimeField(verbose_name='fecha de renta')),
                ('fecha_de_Devuelta', models.DateTimeField(verbose_name='fecha de devolucion')),
                ('monto_por_dia', models.FloatField()),
                ('cantidad_de_Dia', models.IntegerField()),
                ('estado', models.CharField(max_length=100)),
                ('comentario', models.CharField(max_length=200)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App1.Clientes')),
                ('empleado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App1.Empleados')),
                ('vehiculo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App1.Vehiculos')),
            ],
            options={
                'verbose_name': 'Renta y Devolucion',
                'verbose_name_plural': 'Rentas y Devoluciones',
            },
        ),
    ]
