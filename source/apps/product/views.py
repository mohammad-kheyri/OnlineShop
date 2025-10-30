from django.shortcuts import render
from django.http import HttpResponse, request
from django.views.generic import ListView, DetailView

from .models import Product, ProductCategory


class IndexView(ListView):
    template_name = 'index.html'
    model = Product
    queryset = Product.objects.all()

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        context['active_page'] = "index"
        # context["product_list"] = Product.objects.all()
        context["new_product"] = Product.objects.last()
        return context

class ProductDetailView(DetailView):
    template_name = 'single-product.html'
    model = Product

    def get_queryset(self):
        return Product.objects.all()


    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        context['active_page'] = 'single-product'
        # context["product"] = Product.objects.get(id=self.kwargs.get("pk"))
        return context

class ProductListView(ListView):
    template_name = 'category.html'
    model = ProductCategory

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        context['active_page'] = "products"
        return context



# def product_details(request):
#     return render(request, 'single-product.html')


# def index(request):
#     return render(request, 'index.html')


# def category(request):
#     return render(request, 'category.html')


