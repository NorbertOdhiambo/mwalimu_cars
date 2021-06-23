from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import *
from cloudinary.forms import CloudinaryFileField


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class ProductForm(forms.ModelForm):
    more_images = forms.ImageField(required=False, widget=forms.ClearableFileInput(attrs={
        "class": "form-control",
        "multiple": True
    }))

    image = CloudinaryFileField(options={
        "tags": "directly_uploaded"
    })

    class Meta:
        model = Product
        fields = ['make', 'model', 'new_or_used', 'cc', 'car_brand', 'latest', 'slug', 'colour', 'body_type',
                  'interior', 'transmission', 'mileage', 'fuel', 'year', 'price', 'negotiable', 'image', 'description']

        widgets = {
            "make": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Enter the vehicle's make here..."
            }),
            "model": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Enter the car model here..."
            }),
            "new_or_used": forms.CheckboxInput(attrs={
                "class": "myonoffswitch",
                'id': 'myonoffswitch'
                # "placeholder": "Check box if car is new..."
            }),
            "cc": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Enter the engine capacity here..."
            }),
            "latest": forms.CheckboxInput(attrs={
                "class": "myonoffswitch",
                'id': 'myonoffswitch'
                # "placeholder": "Check box if car is latest..."
            }),
            "slug": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Enter the unique slug here..."
            }),
            "colour": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Enter car's colour..."
            }),
            "body_type": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Enter body type..."
            }),
            "interior": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "How does the vehicle's interior look? (e.g leather seats)..."
            }),
            "transmission": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Enter transmission..."
            }),
            "mileage": forms.TextInput(attrs={
                "class": "form-control"
            }),
            "fuel": forms.TextInput(attrs={
                "class": "form-control"
            }),
            "year": forms.TextInput(attrs={
                "class": "form-control"
            }),
            "price": forms.TextInput(attrs={
                "class": "form-control"
            }),
            "negotiable": forms.CheckboxInput(attrs={
                'class': 'onoffswitch', 'id': 'myonoffswitch'
            }),
            # "image": CloudinaryFileField(options={
            #     "tags": "directly_uploaded"
            # }),
            "description": forms.Textarea(attrs={
                "class": "form-control",
                "placeholder": "Give a brief description of the car...like chairs/seat quality",
            }),

        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'body')


# class CustomerForm(forms.ModelForm):
#     class Meta:
#         model = Customer
#         fields = ['user', 'full_name', 'joined_on']
#
#
# class OrderForm(forms.ModelForm):
#     class Meta:
#         model = Order
#         fields = ['order_by', 'ordered_item', 'ordering_happened_on']
