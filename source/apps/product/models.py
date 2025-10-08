from django.db import models

from apps.user.models import User


class Brand(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    

class Color(models.Model):
    name = models.CharField(max_length=100)


    def __str__(self):
        return self.name
    
class ProductCategory(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    color = models.ForeignKey(Color, on_delete=models.CASCADE)
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class ProductComment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.product
    

class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.product