# Generated by Django 5.1.2 on 2024-10-24 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0013_producto_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categoria',
            name='referencia_categoria',
            field=models.CharField(max_length=10),
        ),
    ]
