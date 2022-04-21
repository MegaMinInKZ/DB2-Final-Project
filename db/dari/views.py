import cx_Oracle
from django.shortcuts import render
from django.http import HttpResponse
import requests
from bs4 import BeautifulSoup
from .models import *
import random
import csv
def home(request):
    html = "<html><body>It is now %s.</body></html>"
    return HttpResponse(html)

def product(request, pk):
    product = Product.objects.get(pk=pk)
    prices = Price_History.objects.filter(product_id=pk)
    amo_rating = cx_Oracle.connect('DB', 'db').cursor().callfunc("amount_rating_product", int, [1])
    context = {
        'price_history': prices,
        'product': product,
        'rating': amo_rating
    }
    return render(request, 'product/product.html', context)


# Create your views here.
