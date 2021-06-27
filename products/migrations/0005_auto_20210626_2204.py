# Generated by Django 3.2.4 on 2021-06-26 19:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_delete_test'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feature',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('features', models.CharField(max_length=255)),
            ],
        ),
        migrations.AlterField(
            model_name='product',
            name='body_type',
            field=models.CharField(blank=True, choices=[('Hatchback', 'Hatchback'), ('Convertible', 'Convertible'), ('Coupe', 'Coupe'), ('Sedan', 'Sedan'), ('Sports car', 'Sports car'), ('Notchback', 'Notchback'), ('SUV', 'SUV'), ('Luxury', 'Luxury'), ('Station wagon/Estate car', 'Station wagon/Estate car'), ('Super car', 'Super car'), ('MUV', 'MUV'), ('Pickup truck/Pickup', 'Pickup truck/Pickup'), ('Minivan/Van', 'Minivan/Van'), ('Crossover', 'Crossover'), ('Buggy', 'Buggy')], max_length=100),
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='transmission',
            field=models.CharField(blank=True, choices=[('Automatic', 'Automatic'), ('Manual', 'Manual')], max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='features',
            field=models.ManyToManyField(blank=True, null=True, to='products.Feature'),
        ),
    ]