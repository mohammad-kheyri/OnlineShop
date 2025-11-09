from django.urls import path
from .views import CartView, AddToCartView, RemoveFromCartView, CheckoutView, ConfirmationView

app_name = 'transaction'

urlpatterns = [
    path('cart/', CartView.as_view(), name='cart'),
    path('cart/add/<int:product_id>/', AddToCartView.as_view(), name='add_to_cart'),
    path('cart/remove/<int:item_id>/', RemoveFromCartView.as_view(), name='remove_from_cart'),
    path('checkout/', CheckoutView.as_view(), name='checkout'),
    path('confirmation/', ConfirmationView.as_view(), name='confirmation'),
]