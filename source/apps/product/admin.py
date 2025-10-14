from django.contrib import admin

from .models import Brand, Color, ProductCategory, Product, ProductComment, Review


@admin.register(Product)
class AdminProduct(admin.ModelAdmin):
    list_display = ('name', 'original_price', 'off_price', 'brand', 'color', 'category')
    search_fields = ('name',)
    list_filter = ('brand', 'color', 'category')

    # This lets you pick or add Brands, Colors, etc., directly
    autocomplete_fields = ['brand', 'color', 'category']


@admin.register(Brand)
class AdminBrand(admin.ModelAdmin):
    search_fields = ['name']


@admin.register(Color)
class AdminColor(admin.ModelAdmin):
    search_fields = ['name']


@admin.register(ProductCategory)
class AdminProductCategory(admin.ModelAdmin):
    search_fields = ['name']

@admin.register(ProductComment)
class AdminProductComment(admin.ModelAdmin):
    search_fields = ['name']

@admin.register(Review)
class AdminReview(admin.ModelAdmin):
    search_fields = ['name']

