from typing import Any
from django.db.models.base import Model as Model
from django.db.models.query import QuerySet
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from django.db.models import Q
from .models import Blog, BlogCategory, BlogTag


class BlogView(ListView):
    template_name = 'blog.html'
    model = Blog
    queryset = Blog.objects.all()
    paginate_by = 4



    def get_queryset(self):
        queryset = super().get_queryset()
        category_id = self.request.GET.get('category')
        tag_id = self.request.GET.get('tag')
        search_query = self.request.GET.get('search')

        if category_id:
            queryset = queryset.filter(category_id=category_id)  # Filtering by category foreign key
    
        tag_id = self.request.GET.get('tag')
        if tag_id:
            queryset = queryset.filter(blogtag=tag_id)


        if search_query:
            queryset = queryset.filter(
                Q(title__icontains=search_query) |
                Q(author__email__icontains=search_query) |
                Q(author__first_name__icontains=search_query) |
                Q(author__last_name__icontains=search_query) 
            )

        return queryset

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        context['active_page'] = 'blog'
        context['categories'] = BlogCategory.objects.all()
        context['selected_category'] = self.request.GET.get('category')
        context['tags'] = BlogTag.objects.all()
        context['selected_tag'] = self.request.GET.get('tag')
        context['search_query'] = self.request.GET.get('search', '')
        return context
        
class BlogDetailsView(DetailView):
    template_name = 'single-blog.html'
    model = Blog
    
    def get_queryset(self):
        return Blog.objects.all()
    
    def get_context_data(self, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        blog = self.get_object()

        context['next_blog'] = Blog.objects.filter(id__gt=blog.id).order_by('id').first()
        context['prev_blog'] = Blog.objects.filter(id__lt=blog.id).order_by('-id').first()
        context["blog_list"] = Blog.objects.all()


        context['active_page'] = 'blog'
        return context 



# def blog(request):
#     return render(request, 'blog.html')



# def blog_details(request):
#     return render(request, 'single-blog.html')


