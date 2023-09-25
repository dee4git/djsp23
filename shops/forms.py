from django import forms

from shops.models import Shop


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