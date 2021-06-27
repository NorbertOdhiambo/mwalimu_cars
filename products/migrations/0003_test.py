# Generated by Django 3.2.4 on 2021-06-26 16:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20210623_1219'),
    ]

    operations = [
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(unique=True)),
                ('brands', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='products.brand')),
            ],
        ),
    ]