import cx_Oracle
from django.shortcuts import render
from django.http import HttpResponse
import requests
from bs4 import BeautifulSoup
from .models import *
import random
import csv
from .db_views import *


def index(request):
    top_rating = TOP_10.objects.all()
    categories = Category.objects.all()
    context = {
        'top_rating': top_rating,
        'categories': categories
    }
    return render(request, 'product/index.html', context)
def category(request):
    cat = Category.objects.get(slug=slug)
    products = Product.objects.filter(category=cat)
    context = {
        'products': products,
    }
    return render(request, 'product/category.html', context)

def product(request, pk):
    product = Product.objects.get(pk=pk)
    prices = Price_History.objects.filter(product_id=pk)
    context = {
        'price_history': prices,
        'product': product,
    }
    return render(request, 'product/product.html', context)


# Create your views here.
