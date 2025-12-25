from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, JsonResponse
from django.views import View
from .models import Cart, ProductCart, BillingDetails
from apps.product.models import Product
from apps.user.models import Customer
from .forms import BillingForm
import json



class CartView(View):
    def get(self, request):
        customer = get_object_or_404(Customer, user=request.user.id)
        cart, created = Cart.objects.get_or_create(customer=customer)
        return render(request, 'cart.html', {'cart': cart})


class AddToCartView(View):
    def post(self, request, product_id):
        product = get_object_or_404(Product, id=product_id)
        cart, created = Cart.objects.get_or_create(customer=request.user.customer)
        data = json.loads(request.body)
        quantity = data.get("quantity")
        print(quantity)
        if not quantity:
            quantity = 1
        product_cart, created = ProductCart.objects.get_or_create(cart=cart, product=product)
        if created:
            quantity -= 1
        if quantity > 0:
            product_cart.quantity += quantity
            product_cart.save()
        return JsonResponse({"message": "Producat have been added to the your cart"})


class RemoveFromCartView(View):
    def post(self, request, item_id):
        item = get_object_or_404(ProductCart, id=item_id)
        cart_id = item.cart.id
        item.delete()
        return redirect('cart')


class CheckoutView(View):
    def get(self, request):
        cart = get_object_or_404(Cart, customer=request.user.customer)
        billing_details = BillingDetails.objects.filter(user=request.user)
        form = BillingForm()
        
      
        return render(request, 'checkout.html', {
            'cart': cart,
            'form': form
        })

    def post(self, request):
        cart = get_object_or_404(Cart, customer=request.user.customer)

        billing_details = BillingDetails.objects.filter(user=request.user)
        form = BillingForm(request.POST)

        if form.is_valid():
            billing = form.save(commit=False)
            billing.user = request.user
            billing.save()

            cart.is_ordered = True
            cart.save()

            return redirect('transaction:confirmation')

        return render(request, 'checkout.html', {
            'cart': cart,
            'form': form,
        })
    
 

  

 

class ConfirmationView(View):
    def get(self, request):
        customer = get_object_or_404(Customer, user=request.user.id)
        cart = Cart.objects.filter(customer=customer, is_ordered=True).last()
        billing = BillingDetails.objects.filter(user=request.user).last()
        return render(request, 'confirmation.html', {
            'cart': cart,
            'billing': billing
        })
