# Generated by Django 3.2.4 on 2021-06-19 08:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('car_brand', models.CharField(max_length=250)),
                ('slug', models.SlugField(unique=True)),
                ('logo_image', models.ImageField(blank=True, null=True, upload_to='images/logo_img')),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=150)),
                ('joined_on', models.DateTimeField(default=django.utils.timezone.now)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='LogoAnimation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('video', models.FileField(null=True, upload_to='images/animate_logo', verbose_name='')),
            ],
        ),
        migrations.CreateModel(
            name='Poster',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
                ('poster_1', models.ImageField(blank=True, null=True, upload_to='images/posters/')),
                ('poster_2', models.ImageField(blank=True, null=True, upload_to='images/posters/')),
                ('poster_3', models.ImageField(blank=True, null=True, upload_to='images/posters/')),
                ('poster_4', models.ImageField(blank=True, null=True, upload_to='images/posters/')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('make', models.CharField(max_length=255)),
                ('model', models.CharField(max_length=255)),
                ('new_or_used', models.BooleanField(blank=True, default=False, null=True)),
                ('cc', models.CharField(max_length=20)),
                ('latest', models.BooleanField(blank=True, default=False, null=True)),
                ('slug', models.SlugField(unique=True)),
                ('colour', models.CharField(max_length=20)),
                ('body_type', models.CharField(max_length=20)),
                ('interior', models.CharField(max_length=30)),
                ('transmission', models.CharField(max_length=30)),
                ('mileage', models.CharField(max_length=10)),
                ('fuel', models.CharField(max_length=20)),
                ('year', models.CharField(max_length=10)),
                ('price', models.CharField(max_length=20)),
                ('negotiable', models.BooleanField(blank=True, default=False, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='images')),
                ('description', models.TextField(null=True)),
                ('view_count', models.PositiveIntegerField(default=0)),
                ('upload_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('car_brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.brand')),
            ],
            options={
                'db_table': 'pymcars_product',
            },
        ),
        migrations.CreateModel(
            name='SliderArrows',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('arrow_imgs', models.ImageField(blank=True, null=True, upload_to='images/slider_arrows/')),
            ],
        ),
        migrations.CreateModel(
            name='ProductImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images/sub_images/')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.product')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ordering_happened_on', models.DateTimeField(default=django.utils.timezone.now)),
                ('name', models.CharField(blank=True, max_length=150, null=True)),
                ('phone_no', models.CharField(blank=True, max_length=20, null=True)),
                ('email_address', models.EmailField(blank=True, max_length=254, null=True)),
                ('address', models.CharField(blank=True, max_length=50, null=True)),
                ('customer_scheduled_date', models.CharField(blank=True, max_length=100, null=True)),
                ('order_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='products.customer')),
                ('ordered_item', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='products.product')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('body', models.TextField()),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('active', models.BooleanField(default=False)),
                ('post', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='products.product')),
            ],
            options={
                'db_table': 'pymcars_comment',
            },
        ),
    ]