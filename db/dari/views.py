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


# Create your views here.
