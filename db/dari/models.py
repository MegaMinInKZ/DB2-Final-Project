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

    def get_absolute_url(self):
        return reverse('category', kwargs={'slug': self.slug})
class Product(models.Model):
    title = models.CharField(max_length=255)
    upload_date = models.DateField(auto_now_add=True)
    update_date = models.DateField(auto_now=True)
    price = models.IntegerField()
    amount = models.IntegerField()
    Image = models.URLField(max_length = 200)
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

class Rating(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    day = models.DateField(auto_now_add=True)
    value = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])

class Price_History(models.Model):
    price = models.IntegerField()
    day = models.DateField(auto_now_add=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

class Comment(models.Model):
    comment_text = models.TextField()
    day = models.DateField(auto_now_add=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class Cart(models.Model):
    day = models.DateField(auto_now_add=True)
    amount = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    def get_total_price(self):
        return self.amount * self.product.price

class Purchase(models.Model):
    day = models.DateField(auto_now_add=True)
    amount = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    transaction = models.FileField(null=True)
    total_price = models.IntegerField()

class Feedback(models.Model):
    feedback_text = models.TextField()
    day = models.DateField(auto_now_add=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)



