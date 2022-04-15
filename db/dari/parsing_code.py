import requests
from bs4 import BeautifulSoup
import random
import csv

# Category.objects.create(name="Красота и гигиена").save()

endpoint = "https://europharma.kz/catalog/lekarstvennye-sredstva?segment=available"
get_request = requests.get(endpoint)
list_name = BeautifulSoup(get_request.text, "html.parser").find_all('a', class_='card-product__link')
list_image = BeautifulSoup(get_request.text, "html.parser").find_all('img', class_='card-product__img')
list_price = BeautifulSoup(get_request.text, "html.parser").find_all('span', class_='card-product__price_discount')

for i in range(30):
    price_str = list_price[i].decode_contents();
    price_sub1 = price_str.replace('₸', '')
    price_sub2 = price_sub1.replace(' ', '')
    Product.objects.create(title=list_name[i].decode_contents(), price=int(price_sub2), amount=random.randint(10, 100),
                                  image=list_image[i]['src'],category=1).save()