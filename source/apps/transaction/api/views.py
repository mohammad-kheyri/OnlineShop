from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404

from apps.transaction.models import Cart, ProductCart
from apps.product.models import Product
from .serializers import CartSerializer


class CartAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        cart, _ = Cart.objects.get_or_create(customer=request.user.customer)
        serializer = CartSerializer(cart)
        return Response(serializer.data)



class AddToCartAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, product_id):
        cart, _ = Cart.objects.get_or_create(customer=request.user.customer)
        product = get_object_or_404(Product, id=product_id)

        quantity = request.data.get('quantity', 1)

        item, created = ProductCart.objects.get_or_create(
            cart=cart,
            product=product
        )

        if not created:
            item.quantity += int(quantity)
        else:
            item.quantity = int(quantity)

        item.save()

        return Response({
            "message": "Product added to cart",
            "cart": CartSerializer(cart).data
        })

class RemoveFromCartAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, item_id):
        item = get_object_or_404(
            ProductCart,
            id=item_id,
            cart__customer=request.user.customer
        )
        item.delete()

        return Response({"message": "Item removed"})


class CheckoutAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        cart = get_object_or_404(Cart, customer=request.user.customer)

        cart.is_ordered = True
        cart.save()

        return Response({
            "message": "Order placed successfully",
            "cart_id": cart.id
        })
