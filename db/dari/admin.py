from django.contrib import admin
from .models import *
# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'category', 'is_active', 'amount', 'price', 'upload_date')
    list_display_links = ('title', 'id')
    search_fields = ['title']
    list_editable = ('is_active', 'amount', 'price')
    list_filter = ('is_active', 'category', 'upload_date')

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'slug')
    list_display_links = ('id', 'name')
    search_fields = ['name']

class Comment_FeedbackAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'product', 'day')
    list_display_links = ('id',)

class Purchase_CartAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'product', 'day', 'amount')
    list_display_links = ('id',)

class PriceHistoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'product', 'price', 'day')
    list_display_links = ('id',)

class RatingAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'product', 'day', 'value')
    list_display_links = ('id', )



admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Rating, RatingAdmin)
admin.site.register(Price_History, PriceHistoryAdmin)
admin.site.register(Comment, Comment_FeedbackAdmin)
admin.site.register(Cart, Purchase_CartAdmin)
admin.site.register(Purchase, Purchase_CartAdmin)
admin.site.register(Feedback, Comment_FeedbackAdmin)