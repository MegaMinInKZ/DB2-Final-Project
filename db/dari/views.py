import cx_Oracle
from django.shortcuts import render, redirect
from django.http import HttpResponse
import requests
from bs4 import BeautifulSoup
from .models import *
import random
import csv
from .db_views import *
from .forms import *
from django.contrib.auth import authenticate, login, logout
from django.http import FileResponse



context = {}
def index(request):
    top_rating = TOP_10.objects.all()
    categories = Category.objects.all()
    context = {
        'title': "Home page",
        'top_rating': top_rating,
        'categories': categories
    }
    return render(request, 'product/index.html', context)
def category(request):
    cat = Category.objects.get(slug=slug)
    products = Product.objects.filter(category=cat)
    context = {
        'title': cat.title,
        'products': products,
    }
    return render(request, 'product/category.html', context)

def product(request, pk):
    product = Product.objects.get(pk=pk)
    prices = Price_History.objects.filter(product_id=pk)
    comments = Comment.objects.filter(product_id=pk)
    context = {
        'title': product.title,
        'price_history': prices,
        'product': product,
        'comments': comments,
    }
    purchase = Purchase.objects.filter(product_id=pk)
    if purchase:
        reviews = Feedback.objects.filter(purchase_id=purchase.pk)[0]
        context['reviews'] = reviews
    else:
        context['reviews'] = Feedback.objects.filter(pk=-1)
    return render(request, 'product/product.html', context)

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(request, username=username, password=password)
            login(request, user)
            return redirect('login')
        else:
            context['first_name'] = request.POST.get('first_name')
            context['last_name'] = request.POST.get('last_name')
            context['username'] = request.POST.get('username')
            context['email'] = request.POST.get('email')
            context['error'] = True

    return render(request, 'product/register.html', context)

def login_(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            context['error'] = "Invalid username or password"
            context['username'] = request.POST.get('username')
            return render(request, 'product/login.html', context)
    return render(request, 'product/login.html')

def transaction(request):
    purchase_id = request.POST.get('purchase_id')
    object_name = Purchase.objects.get(pk=purchase_id)
    filename = object_name.transaction.name.split('/')[-1]
    response = HttpResponse(object_name.transaction, content_type='text/plain')
    response['Content-Disposition'] = 'attachment; filename=%s' % filename

    return response
def test(request):
    user = User.objects.get(pk=2)
    product = Product.objects.get(pk=3)
    x = Purchase.objects.create(amount=1, user=user, product=product)
    x.transaction = 'purchase/'+ str(x.pk) + '.txt'
    x.save()
# Create your views here.
