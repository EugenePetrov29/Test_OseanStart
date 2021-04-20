from django.urls import path

from .views import (ProductListView, ProductCreateView, ProductDetailView, ProductDeletedListView, ProductPublishedListView,
                    ProductPriceListView, ProductCategoriesListView, CategoryListView, CategoryCreateView,
                    ProductDeleteView, CategoryDeleteView, ProductNameListView)

urlpatterns = [
    path('products/create', ProductCreateView.as_view(), name='product_create'),
    path('products/all', ProductListView.as_view(), name='product_all'),
    path('products/not-deleted', ProductDeletedListView.as_view(), name='product_not-delete'),
    path('products/published', ProductPublishedListView.as_view(), name='product_published'),
    path('products/price', ProductPriceListView.as_view(), name='product_price'),
    path('products/categories', ProductCategoriesListView.as_view(), name='product_categories'),
    path('products/detail/<int:pk>', ProductDetailView.as_view(), name='product_detail'),
    path('categories/all', CategoryListView.as_view(), name='categories_all'),
    path('categories/create', CategoryCreateView.as_view(), name='categories_create'),
    path('categories/delete/<int:pk>', CategoryDeleteView.as_view(), name='categories_delete'),
    path('products/delete/<int:pk>', ProductDeleteView.as_view(), name='product_delete'),
    path('products/name', ProductNameListView.as_view(), name='product_name'),
]
