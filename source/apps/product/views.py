from django.shortcuts import render
from django.http import HttpResponse, request
from django.views.generic import ListView, DetailView

from .models import Product, ProductCategory


class ProductView(ListView):
    template_name = 'index.html'
    model = Product
    queryset = Product.objects.all()

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        context['active_page'] = Product.objects.all()

class ProductDetailView(DetailView):
    template_name = 'single-product.html'
    model = Product

    def get_queryset(self):
        return Product.objects.all()

class CategoryListView(ListView):
    template_name = 'category.html'
    model = ProductCategory




# def product_details(request):
#     return render(request, 'single-product.html')


# def index(request):
#     return render(request, 'index.html')


# def category(request):
#     return render(request, 'category.html')


