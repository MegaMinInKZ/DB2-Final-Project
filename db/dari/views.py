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
def category(request, slug):
    cat = Category.objects.get(slug=slug)
    products = Product.objects.filter(category=cat)
    context = {
        'title': cat.name,
        'products': products,
    }
    return render(request, 'product/_category_page.html', context)

def product(request, pk):
    product = Product.objects.get(pk=pk)
    prices = Price_History.objects.filter(product_id=pk)
    comments = Comment.objects.filter(product_id=pk)
    context = {
        'title': product.title,
        'price_history': prices,
        'product': product,
        'comments': comments,
        'reviews': Feedback.objects.filter(product=product)
    }
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

def logout_(request):
    logout(request)
    return redirect('home')

def transaction(request):
    purchase_id = request.POST.get('purchase_id')
    object_name = Purchase.objects.get(pk=purchase_id)
    filename = object_name.transaction.name.split('/')[-1]
    response = HttpResponse(object_name.transaction, content_type='text/plain')
    response['Content-Disposition'] = 'attachment; filename=%s' % filename
    return response


def basket(request):
    if request.user:
        carts = Cart.objects.filter(user=request.user)
        context = {
            'title': 'My carts',
            'carts': carts
        }
        return render(request, 'product/basket.html', context)
    return redirect('login')

def add_to_basket(request):
    if request.method == "POST":
        Cart.objects.create(amount=request.POST.get('amount'), user=request.user, product=Product.objects.get(pk=request.POST.get('product_id'))).save();
        redirect('basket')
    return redirect('basket')


def profile(request):
    purchases = Purchase.objects.filter(user=request.user)
    context = {
        'title': "My Profile",
        'purchases': purchases,
    }
    return render(request, 'product/profile.html', context)

def edit_profile(request):
    if request.method == "POST":
        user_form = UpdateUserForm(request.POST, instance=request.user)
        if user_form.is_valid():
            user_form.save()
            return redirect('profile')
        else:
            context['error'] = "Enter unique username and email, also check out first name and last name accuracy"
    return render(request, 'product/edit_profile.html', context)
def update_cart(request):
    if request.method == "POST":
        cart_id = request.POST.get('cart_id')
        cart = Cart.objects.get(pk=cart_id)
        cart.amount = request.POST.get('amount')
        cart.save()
    return redirect('basket')

def delete_cart(request):
    if request.method == "POST":
        cart_id = request.POST.get('cart_id')
        Cart.objects.filter(pk=cart_id).delete()
    return redirect('basket')

def buy(request):
    if request.method == "POST":
        cart = Cart.objects.get(pk=request.POST.get('cart_id'))
        purchase = Purchase.objects.create(amount=cart.amount, user=cart.user, product=cart.product, total_price=cart.product.price * cart.amount)
        purchase.transaction = "purchase/" + str(purchase.pk) + ".txt"
        purchase.save()
        Feedback.objects.create(user=request.user, feedback_text=request.POST.get('feedback'), product=cart.product).save()
        Rating.objects.create(user=request.user, value=request.POST.get('rating'), product=cart.product).save()
    return redirect('profile')


def check(request):
    return FileResponse(Purchase.objects.get(pk=request.POST.get('purchase_id')).transaction, as_attachment=True, filename='purchase.txt')

# Create your views here.
