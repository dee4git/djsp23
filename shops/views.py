from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from . import forms
from .models import Shop, Product


# Create your views here.
def create_shop(request):
    if request.method == 'GET':
        form = forms.ShopCreationForm(request.GET or None)
        print('form is created')
        if form.is_valid():
            form.save()
            return HttpResponse('created successfully')
    else:
        form = forms.ShopCreationForm()
    return render(request, 'form.html', {
        "form": form
    })


def update_shop(request, s_id):
    shop = get_object_or_404(Shop, pk=s_id)
    if request.method == 'GET':
        form = forms.ShopUpdationForm(request.GET or None, instance=shop)
        if form.is_valid():
            form.save()
            return HttpResponse('updated successfully')
    else:
        form = forms.ShopUpdationForm(instance=shop)
    return render(request, 'form.html', {
        "form": form
    })


def delete_shop(request, s_id):
    Shop.objects.get(pk=s_id).delete()
    return redirect('/')


def view_products(request, s_id):
    shop = Shop.objects.get(pk=s_id)
    products = Product.objects.filter(shop=shop)
    return render(request, 'view-products.html',
                  {
                      "products": products,
                      "shop": shop,
                  }
                  )


def create_product(request, s_id):
    shop = Shop.objects.get(pk=s_id)
    if request.method == 'GET':
        form = forms.ProductCreationForm(request.GET or None)
        print('form is created')
        if form.is_valid():
            instance = form.save(commit=False)
            instance.shop = shop
            form.save()
            return HttpResponse('created successfully')
    else:
        form = forms.ShopCreationForm()
    return render(request, 'form.html', {
        "form": form
    })


def update_product(request, p_id):
    product = get_object_or_404(Product, pk=p_id)
    if request.method == 'GET':
        form = forms.ProductUpdationForm(request.GET or None, instance=product)
        if form.is_valid():
            form.save()
            return HttpResponse('updated successfully')
    else:
        form = forms.ShopUpdationForm(instance=product)
    return render(request, 'form.html', {
        "form": form
    })
