# Generated by Django 3.2.4 on 2021-06-26 19:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_auto_20210626_2204'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='interior',
        ),
    ]
