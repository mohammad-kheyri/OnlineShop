from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from .models import Cart, ProductCart, BillingDetails
from apps.product.models import Product
from apps.user.models import Customer

# ------------------------------
# CART VIEWS
# ------------------------------
class CartView(View):
    def get(self, request):
        cart, created = Cart.objects.get_or_create(customer=request.user.customer, is_ordered=False)
        return render(request, 'cart.html', {'cart': cart})


class AddToCartView(View):
    def post(self, request, product_id):
        product = get_object_or_404(Product, id=product_id)
        cart, created = Cart.objects.get_or_create(customer=request.user.customer, is_ordered=False)

        product_cart, created = ProductCart.objects.get_or_create(cart=cart, product=product)
        if not created:
            product_cart.quantity += 1
            product_cart.save()

        return redirect('cart')


class RemoveFromCartView(View):
    def post(self, request, item_id):
        item = get_object_or_404(ProductCart, id=item_id)
        cart_id = item.cart.id
        item.delete()
        return redirect('cart')


# ------------------------------
# CHECKOUT VIEWS
# ------------------------------
class CheckoutView(View):
    def get(self, request):
        cart = get_object_or_404(Cart, customer=request.user.customer, is_ordered=False)
        billing_details = BillingDetails.objects.filter(user=request.user).first()
        return render(request, 'checkout.html', {
            'cart': cart,
            'billing_details': billing_details
        })

    def post(self, request):
        cart = get_object_or_404(Cart, customer=request.user.customer, is_ordered=False)
        # Save billing info
        BillingDetails.objects.create(
            user=request.user,
            phone_number=request.POST.get('number'),
            address_line1=request.POST.get('add1'),
            address_line2=request.POST.get('add2'),
            city=request.POST.get('city'),
            country=request.POST.get('country', 'Country'),  # optional
            postal_code=request.POST.get('zip')
        )
        cart.is_ordered = True
        cart.save()
        return redirect('confirmation')


# ------------------------------
# CONFIRMATION VIEWS
# ------------------------------
class ConfirmationView(View):
    def get(self, request):
        cart = Cart.objects.filter(customer=request.user.customer, is_ordered=True).last()
        billing = BillingDetails.objects.filter(user=request.user).last()
        return render(request, 'confirmation.html', {
            'cart': cart,
            'billing': billing
        })
