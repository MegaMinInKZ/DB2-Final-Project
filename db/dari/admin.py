from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Rating)
admin.site.register(Price_History)
admin.site.register(Comment)
admin.site.register(Cart)
admin.site.register(Purchase)
admin.site.register(Feedback)