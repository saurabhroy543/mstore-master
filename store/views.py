from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
from django.core.paginator import Paginator


# Create your views here.
def home(request):
    items = Product.objects.all()

    # paginator code
    ''' paginator = Paginator(items, 1)
    page = paginator.page(1)
    items = paginator.page'''
    return render(request, 'index.html', {'items': items})


def product(request):
    items = Product.objects.all()
    return render(request, 'products.html', {'items': items})


def contact(request):
    return render(request, 'contact.html')
