from typing import Any
from django.db.models.base import Model as Model
from django.db.models.query import QuerySet
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView


from .models import Blog


class BlogView(ListView):
    template_name = 'blog.html'
    model = Blog
    queryset = Blog.objects.all()

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        context['active_page'] = Blog.objects.all().order_by('-created_at')
        return context
        
class BlogDetailsView(DetailView):
    template_name = 'single-blog.html'
    model = Blog
    
    def get_queryset(self):
        return Blog.objects.all()
    


# def blog(request):
#     return render(request, 'blog.html')



# def blog_details(request):
#     return render(request, 'single-blog.html')


