from django.urls import path
from .views import IndexView, ProductDetailView, ProductListView

app_name = "product"

urlpatterns = [
    path('',  IndexView.as_view(), name='index'),
    path('product/', ProductListView.as_view(), name='category'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product_detail')
    
]