from django.db import models
import cx_Oracle
from django.urls import reverse
from django.core.validators import MaxValueValidator, MinValueValidator
from .models import Category

class TOP_10(models.Model):
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