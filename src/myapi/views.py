from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from .serializers import CategorySerializer, ProductSerializer, ProductDeleteSerializer
from .models import Category, Products
from django.views.generic import TemplateView
# Create your views here.

class ProductDetailView(generics.RetrieveUpdateAPIView):

    serializer_class = ProductSerializer
    queryset = Products.objects.all()

class ProductDeleteView(generics.RetrieveUpdateAPIView):

    '''
    view for Удаление товаров (товар помечается как удаленный).
    изменяет параметр deleted для товара. оставляя его в базе.
    '''
    serializer_class = ProductSerializer
    queryset = Products.objects.all()

    def get(self, request, *args, **kwargs):
        '''
        Переопределенная функция из RetriveUpdateAPIView
        '''
        instance = self.get_object()
        instance.deleted = True
        instance.save()
        return Response({"success": "success"})

class CategoryDeleteView(generics.RetrieveUpdateAPIView):

    '''
    view for Удаление категорий (вернуть ошибку если категория прикреплена к товару)
    изменяет параметр deleted для товара. оставляя его в базе.
    '''
    serializer_class = CategorySerializer
    queryset = Category.objects.all()

    def get(self, request, *args, **kwargs):
        '''
        Переопределенная функция из RetriveUpdateAPIView
        '''
        useless = True
        instance = self.get_object()
        all_products = Products.objects.all()
        for cat in all_products:
            for el in cat.product_categories.all():
                if el.pk == instance.pk:
                    useless = False
                    return Response({"error": "category is applied to a one or a more Product"})
        if useless == True:
            instance.delete()
            instance.save()
            return Response({"success": "success"})

class CategoryCreateView(generics.CreateAPIView):

    serializer_class = CategorySerializer

class CategoryListView(generics.ListAPIView):

    serializer_class = CategorySerializer
    queryset = Category.objects.all()

class ProductListView(generics.ListAPIView):

    serializer_class = ProductSerializer
    queryset = Products.objects.all()

class ProductDeletedListView(generics.ListAPIView):

    serializer_class = ProductSerializer
    queryset = Products.objects.filter(deleted=False)

class ProductPublishedListView(generics.ListAPIView):

    serializer_class = ProductSerializer

    def get_queryset(self):
        queryset = Products.objects.all()
        pub = self.request.query_params.get('status', None)
        print(pub)
        if pub is not None and pub == 'yes':
            queryset = queryset.filter(published=True)
        elif pub is not None and pub == 'no':
            queryset = queryset.filter(published=False)
        return queryset

class ProductPriceListView(generics.ListAPIView):

    serializer_class = ProductSerializer

    def get_queryset(self):
        queryset = Products.objects.all()
        min = self.request.query_params.get('min', None)
        max = self.request.query_params.get('max', None)
        if min is not None and max is not None:
            queryset = queryset.filter(product_price__gte=min, product_price__lte=max)
        return queryset

class ProductNameListView(generics.ListAPIView):

    serializer_class = ProductSerializer

    def get_queryset(self):
        queryset = Products.objects.all()
        name = self.request.query_params.get('name', None)
        if name is not None:
            queryset = queryset.filter(product_name__startswith=name)
        return queryset

class ProductCategoriesListView(generics.ListAPIView):

    serializer_class = ProductSerializer
    '''
    categories/all?category=<id>
    '''
    def get_queryset(self):
        result = []
        queryset = Products.objects.all()
        category = self.request.query_params.get('category', None)
        if category is not None and category is int:
            queryset = queryset.filter(product_categories=category)
            return queryset
        elif category.isdigit() == False:
            for obj in queryset:
                for el in obj.categories.all():
                    if el.name.startswith(category):
                        result.append(obj)
            queryset = result
        return queryset

class ProductCreateView(generics.CreateAPIView):
    serializer_class = ProductSerializer

class HomePage(TemplateView):
    template_name ='myapi/home.html'