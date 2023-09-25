from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from . import forms
from .models import Shop


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
