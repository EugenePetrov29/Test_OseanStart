from rest_framework import serializers
from .models import Category, Products

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = ['pk', 'product_name', 'product_price', 'product_categories', 'product_description', 'published', 'deleted']

class ProductListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = '__all__'

class ProductDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = ['name', 'deleted']