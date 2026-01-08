from django.urls import path
from .views import RemoveFromCartAPIView, CartAPIView, AddToCartAPIView, CheckoutAPIView


app_name = 'transaction'

urlpatterns = [
    path('cart/', CartAPIView.as_view()),
    path('cart/add/<int:product_id>/', AddToCartAPIView.as_view()),
    path('cart/remove/<int:item_id>/', RemoveFromCartAPIView.as_view()),
    path('cart/checkout/', CheckoutAPIView.as_view())
]