# Generated by Django 3.0.7 on 2020-06-08 21:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TiposVehiculos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=300)),
                ('estado', models.BooleanField(default=False)),
            ],
        ),
    ]