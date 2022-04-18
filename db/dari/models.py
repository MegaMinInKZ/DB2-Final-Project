from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator



# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=255)
    class Meta:
        verbose_name_plural = 'Categories'
class Product(models.Model):
    title = models.CharField(max_length=255)
    upload_date = models.DateField(auto_now_add=True)
    price = models.IntegerField()
    amount = models.IntegerField()
    Image = models.URLField(max_length = 200)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

class Rating(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    value = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])

class Price_History(models.Model):
    price = models.IntegerField()
    date = models.DateField(auto_now_add=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

class Comment(models.Model):
    comment_text = models.TextField()
    date = models.DateField(auto_now_add=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class Cart(models.Model):
    date = models.DateField(auto_now_add=True)
    amount = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

class Purchase(models.Model):
    date = models.DateField(auto_now_add=True)
    amount = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

class Feedback(models.Model):
    description = models.TextField()
    date = models.DateField()
    purchase = models.ForeignKey(Purchase, on_delete=models.CASCADE)

