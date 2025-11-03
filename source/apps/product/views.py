from django.shortcuts import render
from django.http import HttpResponse, request
from django.views.generic import ListView, DetailView

from .models import Product, ProductCategory, Brand, Color

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
        context['active_page'] = 'product'
        # context["product"] = Product.objects.get(id=self.kwargs.get("pk"))
        return context


class ProductListView(ListView):
    template_name = 'category.html'
    model = Product

    def get_queryset(self):
        queryset = super().get_queryset()

        # Filter by brand if brand slug or id is passed in the URL
        brand_id = self.request.GET.get('brand')
        if brand_id:
            queryset = queryset.filter(brand__id=brand_id)

        # Optional: Filter by category
        category_id = self.request.GET.get('category')
        if category_id:
            queryset = queryset.filter(category__id=category_id)

        # Optional: Filter by color
        color_id = self.request.GET.get('color')
        if color_id:
            queryset = queryset.filter(color__id=color_id)

        return queryset

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        context['active_page'] = "products"
        all_categories = ProductCategory.objects.prefetch_related("product_set")
        all_brands = Brand.objects.prefetch_related("product_set")
        all_colors = Color.objects.prefetch_related("product_set")

        context["category_list"] = [{'category': cat, 'product_count': cat.product_set.count()} for cat in all_categories]
        context["brand_list"] = [{'brand': brand, 'product_count': brand.product_set.count()} for brand in all_brands]
        context["color_list"] = [{'color': color, 'product_count': color.product_set.count()} for color in all_colors]

        # Pass currently selected filters
        context['selected_brand'] = self.request.GET.get('brand')
        context['selected_category'] = self.request.GET.get('category')
        context['selected_color'] = self.request.GET.get('color')

        return context




# context['brand_list'] = Brand.objects.all()
# context['color_list'] = Color.objects.all()
# context['category_list'] = ProductCategory.objects.all()




# def product_details(request):
#     return render(request, 'single-product.html')


# def index(request):
#     return render(request, 'index.html')


# def category(request):
#     return render(request, 'category.html')


        