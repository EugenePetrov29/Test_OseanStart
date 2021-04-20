from django.contrib import admin
from .models import Category, Products
# Register your models here.
admin.site.register(Category)
#admin.site.register(Products)

@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'display_category')