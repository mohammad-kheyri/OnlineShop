from django.contrib import admin

from .models import Cart, ProductCart, BillingDetails


@admin.register(Cart)
class AdminCart(admin.ModelAdmin):
    search_fields = ['name']


@admin.register(ProductCart)
class AdminProductCart(admin.ModelAdmin):
    search_fields = ['name']

@admin.register(BillingDetails)
class AdminBillingDetails(admin.ModelAdmin):
    search_fields = ['name']
