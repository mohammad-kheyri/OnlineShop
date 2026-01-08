from rest_framework import serializers
from apps.transaction.models import Cart, ProductCart, BillingDetails


class ProductCartSerializer(serializers.ModelSerializer):
    product_name = serializers.CharField(source='product.name', read_only=True)
    product_price = serializers.FloatField(source='product.off_price', read_only=True)
    total_price = serializers.FloatField(read_only=True)

    class Meta:
        model = ProductCart
        fields = [
            'id',
            'product',
            'product_name',
            'product_price',
            'quantity',
            'total_price',
        ]


class CartSerializer(serializers.ModelSerializer):
    items = ProductCartSerializer(many=True, read_only=True)
    total_price = serializers.FloatField(read_only=True)
    total_items = serializers.IntegerField(read_only=True)

    class Meta:
        model = Cart
        fields = [
            'id',
            'customer',
            'is_ordered',
            'total_items',
            'total_price',
            'items',
        ]


class BillingDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = BillingDetails
        fields = '__all__'
