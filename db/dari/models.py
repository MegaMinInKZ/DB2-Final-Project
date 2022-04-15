from django.db import models

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