from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('product/<int:pk>/', product, name='product'),
    path('catedgory/<slug:slug>/', category, name='category'),
    path('login/', login_, name='login'),
    path('register/', register, name='register'),

]
