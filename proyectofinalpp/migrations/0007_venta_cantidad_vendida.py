# Generated by Django 3.2.2 on 2024-09-24 00:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proyectofinalpp', '0006_rename_productostemp_venta_productos'),
    ]

    operations = [
        migrations.AddField(
            model_name='venta',
            name='Cantidad_vendida',
            field=models.FloatField(default=1),
            preserve_default=False,
        ),
    ]