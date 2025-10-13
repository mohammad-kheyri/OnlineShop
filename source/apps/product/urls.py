from django.urls import path
from .views import ProductView, ProductDetailView, CategoryListView


urlpatterns = [
    path('product/',  ProductView.as_view(), name='index'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product-detail'),
    path('category/', CategoryListView.as_view(), name='category')
]