# Generated by Django 3.2.4 on 2021-06-26 20:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_remove_product_interior'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='features',
            field=models.ManyToManyField(blank=True, to='products.Feature'),
        ),
    ]
