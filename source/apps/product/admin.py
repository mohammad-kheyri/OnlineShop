from django.contrib import admin

from .models import Brand, Color, ProductCategory, Product, ProductComment, Review


@admin.register(Brand)
class AdminBrand(admin.ModelAdmin):
    pass

@admin.register(Color)
class AdminColor(admin.ModelAdmin):
    pass

@admin.register(ProductCategory)
class AdminProductCategory(admin.ModelAdmin):
    pass

@admin.register(Product)
class AdminProduct(admin.ModelAdmin):
    pass

@admin.register(ProductComment)
class AdminProductComment(admin.ModelAdmin):
    pass

@admin.register(Review)
class AdminReview(admin.ModelAdmin):
    pass