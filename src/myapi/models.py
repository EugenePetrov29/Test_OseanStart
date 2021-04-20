from django.db import models

# Create your models here.
class Category(models.Model):
    category_name = models.CharField(max_length=60)
    category_description = models.TextField()

    def __str__(self):
        return self.category_name

class Products(models.Model):
    product_name = models.CharField(max_length=60)
    product_categories = models.ManyToManyField(Category, related_name='Categories')
    product_price = models.IntegerField(verbose_name='Price', default='0')
    product_description = models.TextField(default='')
    published = models.BooleanField(default='False')
    deleted = models.BooleanField(default='False')

    def __str__(self):
        return self.product_name

    def display_category(self):
        return ', '.join([category.category_name for category in self.product_categories.all()[:3] ])
    display_category.short_description = 'Category'