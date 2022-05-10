from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('product/<int:pk>/', product, name='product'),
    path('catedgory/<slug:slug>/', category, name='category'),
    path('login/', login_, name='login'),
    path('register/', register, name='register'),
    path('transaction/', transaction, name='transaction'),
    path('my-basket/', basket, name='basket'),
    path('my-profile/', profile, name='profile'),
    path('logout/', logout_, name='logout'),
    path('edit-profile', edit_profile, name='edit-profile'),
    path('add-to-basket', add_to_basket, name='add-to-basket'),
    path('update-cart/', update_cart, name='update-cart'),
    path('delete-cart/', delete_cart, name='delete-cart'),
    path('buy/', buy, name='buy'),
    path('check/', check, name='check'),
]
