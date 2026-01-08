from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .serializers import ProductSerializers, ProductDetailSerializers
from apps.product.models import Product

class ProductViewSet(viewsets.ModelViewSet):

    queryset = Product.objects.all()
    serializer_class = ProductSerializers
    permission_classes = [IsAuthenticated]


class ProductDetailViewSet(viewsets.ModelViewSet):
    
    queryset = Product.objects.all()
    serializer_class = ProductDetailSerializers
    permission_classes = [IsAuthenticated]