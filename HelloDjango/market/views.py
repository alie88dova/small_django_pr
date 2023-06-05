from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import ProductInfo
from .forms import *
# Create your views here.

def market(request):
    pr = ProductInfo.objects.all()
    if request.method=='POST':
        form = AddProductForm(request.POST)
        if form.is_valid():
            try:
                ProductInfo.objects.create(**form.cleaned_data)
            except Exception as e:
                print(e)
    form = AddProductForm()
    return render(request, 'market.html', {"title":"Магазин Supply",
                                          'products': pr,
                                          'form': form})

def card_info(request, cardname):
    return HttpResponse(f'Card {cardname}')