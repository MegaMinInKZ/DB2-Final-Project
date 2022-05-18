from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.urls import reverse
import cx_Oracle





# Create your models here.
class Category(models.Model):
    slug = models.SlugField(max_length=255)
    image = models.ImageField(upload_to='category/')
    name = models.CharField(max_length=255)
    class Meta:
        verbose_name_plural = 'Categories'
        ordering = ['name']

    def get_absolute_url(self):
        return reverse('category', kwargs={'slug': self.slug})
    def __str__(self):
        return self.name
class Product(models.Model):
    title = models.CharField(max_length=255)
    upload_date = models.DateField(auto_now_add=True)
    update_date = models.DateField(auto_now=True)
    price = models.IntegerField(validators=[MinValueValidator(0)])
    amount = models.IntegerField(validators=[MinValueValidator(0)])
    Image = models.ImageField(upload_to='product/%Y/%m/%d')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)

    def get_absolute_url(self):
        return reverse('product', kwargs={'pk': self.pk})
    def get_rating(self):
        return cx_Oracle.connect('DB', 'db').cursor().callfunc("average_rating_product", float, [self.pk])
    def get_rating_count(self):
        return cx_Oracle.connect('DB', 'db').cursor().callfunc("amount_rating_product", int, [self.pk])
    def get_comment_count(self):
        return cx_Oracle.connect('DB', 'db').cursor().callfunc("amount_comment_product", int, [self.pk])
    def get_feedback_count(self):
        return cx_Oracle.connect('DB', 'db').cursor().callfunc("amount_feedback_product", int, [self.pk])
    def __str__(self):
        return self.title;
    class Meta:
        ordering = ['upload_date']

class Rating(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    day = models.DateField(auto_now_add=True)
    value = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])

    class Meta:
        ordering = ['day']
class Price_History(models.Model):
    price = models.IntegerField()
    day = models.DateField(auto_now_add=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    class Meta:
        verbose_name_plural = 'Price History'
        verbose_name = 'Price History'
        ordering = ['day']

class Comment(models.Model):
    comment_text = models.TextField()
    day = models.DateField(auto_now_add=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    def get_day(self):
        return cx_Oracle.connect('DB', 'db').cursor().callfunc("get_day_or_month_comment", str, [self.pk])
    class Meta:
        ordering = ['day']
class Cart(models.Model):
    day = models.DateField(auto_now_add=True)
    amount = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    def get_total_price(self):
        return self.amount * self.product.price
    class Meta:
        ordering = ['day']

class Purchase(models.Model):
    day = models.DateField(auto_now_add=True)
    amount = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    transaction = models.FileField(null=True)
    total_price = models.IntegerField()
    class Meta:
        ordering = ['day']

class Feedback(models.Model):
    feedback_text = models.TextField()
    day = models.DateField(auto_now_add=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    def get_day(self):
        return cx_Oracle.connect('DB', 'db').cursor().callfunc("get_day_or_month_feedback", str, [self.pk])
    class Meta:
        ordering = ['day']


