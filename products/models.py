from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User
from django.utils import timezone


class Brand(models.Model):
    car_brand = models.CharField(max_length=250)
    slug = models.SlugField(unique=True)
    logo_image = models.ImageField(null=True, blank=True, upload_to='images/logo_img')

    def __str__(self):
        return self.car_brand


class Product(models.Model):
    make = models.CharField(max_length=255)
    model = models.CharField(max_length=255)
    new_or_used = models.BooleanField(default=False, null=True, blank=True)
    cc = models.CharField(max_length=20)
    car_brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    latest = models.BooleanField(default=False, null=True, blank=True)
    slug = models.SlugField(unique=True)
    colour = models.CharField(max_length=20)
    body_type = models.CharField(max_length=20)
    interior = models.CharField(max_length=30)
    transmission = models.CharField(max_length=30)
    mileage = models.CharField(max_length=10)
    fuel = models.CharField(max_length=20)
    year = models.CharField(max_length=10)
    price = models.CharField(max_length=20)
    negotiable = models.BooleanField(default=False, null=True, blank=True)
    image = models.ImageField(null=True, blank=True, upload_to='images')
    description = models.TextField(null=True)
    view_count = models.PositiveIntegerField(default=0)
    upload_date = models.DateTimeField(null=True, blank=True, auto_now_add=True)

    class Meta:
        ordering = ['-upload_date']

    def __str__(self):
        return self.make

    class Meta:
        db_table = "pymcars_product"

    def save(self, *args, **kwargs):
        value = self.make
        self.slug = slugify(value, allow_unicode=True)
        super().save(*args, **kwargs)


class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/sub_images/')

    def __str__(self):
        return self.product.make


class LogoAnimation(models.Model):
    name = models.CharField(max_length=20)
    video = models.FileField(null=True, verbose_name="", upload_to='images/animate_logo')

    def __str__(self):
        return self.name + ": " + str(self.video)


class Poster(models.Model):
    name = models.CharField(max_length=25)
    poster_1 = models.ImageField(null=True, blank=True, upload_to='images/posters/')
    poster_2 = models.ImageField(null=True, blank=True, upload_to='images/posters/')
    poster_3 = models.ImageField(null=True, blank=True, upload_to='images/posters/')
    poster_4 = models.ImageField(null=True, blank=True, upload_to='images/posters/')


class SliderArrows(models.Model):
    arrow_imgs = models.ImageField(null=True, blank=True, upload_to='images/slider_arrows/')


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=150)
    joined_on = models.DateTimeField(default=timezone.now)


class Order(models.Model):
    order_by = models.ForeignKey(Customer, on_delete=models.CASCADE, null=True)
    ordering_happened_on = models.DateTimeField(default=timezone.now)
    ordered_item = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=150, null=True, blank=True)
    phone_no = models.CharField(max_length=20, null=True, blank=True)
    email_address = models.EmailField(null=True, blank=True)
    address = models.CharField(max_length=50, null=True, blank=True)
    customer_scheduled_date = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.name


class Comment(models.Model):
    post = models.ForeignKey(Product, on_delete=models.CASCADE, null=True, blank=True, related_name='comments')
    name = models.CharField(max_length=250)
    email = models.EmailField(null=True, blank=True)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return 'Comment {} by {}'.format(self.body, self.name)

    class Meta:
        db_table = "pymcars_comment"
