from django.shortcuts import render

from shops.models import Shop


def home(request):
    shops = Shop.objects.all()
    return render(request, 'home.html', {
        "shops": shops
    })
