# Generated by Django 3.0.7 on 2020-06-16 16:18

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App1', '0011_auto_20200616_1208'),
    ]

    operations = [
        migrations.AlterField(
            model_name='renta_devolucion',
            name='fecha_de_Devuelta',
            field=models.DateTimeField(default=datetime.datetime),
        ),
    ]
