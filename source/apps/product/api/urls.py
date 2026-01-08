from rest_framework.routers import DefaultRouter  
from .views import ProductViewSet, ProductDetailViewSet
from django.urls import path, include

app_name = 'product'

routers = DefaultRouter()
routers.register(r'products', ProductViewSet, basename='products')

routers.register(r'products-detail', ProductDetailViewSet, basename='product-detail')

urlpatterns = [
    path('', include(routers.urls)),
    path('<int:pk>/', include(routers.urls))
]