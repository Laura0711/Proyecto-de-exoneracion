# Generated by Django 3.0.7 on 2020-06-13 02:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App1', '0008_auto_20200612_2140'),
    ]

    operations = [
        migrations.AddField(
            model_name='empleados',
            name='comision',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]
