from django import forms

from shops.models import Shop, Product


class ShopCreationForm(forms.ModelForm):
    class Meta:
        model = Shop
        fields = [
            'name',
            'address',
            'phone',
            'email',
        ]


class ShopUpdationForm(forms.ModelForm):
    class Meta:
        model = Shop
        fields = [
            'name',
            'address',
            'phone',
            'email',
        ]


class ProductCreationForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            'name',
            'quantity',
            'price',
        ]

class ProductUpdationForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            'name',
            'quantity',
            'price',
        ]
