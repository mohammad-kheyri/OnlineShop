from typing import Any
from django.db.models.base import Model as Model
from django.db.models.query import QuerySet
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.db.models import Q
from .models import Blog, BlogCategory, BlogTag, BlogComment
from .forms import BlogCommentForm, CreateBlogForm
from django.urls import reverse_lazy

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
            queryset = queryset.filter(category_id=category_id)
    
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
        context['comment_form'] = BlogCommentForm()
        context['comments'] = BlogComment.objects.filter(blog=self.object).order_by('-created_at')


        context['active_page'] = 'blog'
        return context 



    def post(self, request, *args, **kwargs):
            self.object = self.get_object()
            form = BlogCommentForm(request.POST)
            if form.is_valid():
                comment = form.save(commit=False)
                comment.blog = self.object
                comment.user = request.user  
                comment.save()
                return redirect('blog:blog-detail', pk=self.object.pk) 
            else:
                context = self.get_context_data()
                context['comment_form'] = form
                return self.render_to_response(context)


class CreateBlog(CreateView):
    model = Blog
    form_class = CreateBlogForm
    template_name = 'create-blog.html'
    success_url = reverse_lazy('blog:blog')

    
    def form_valid(self, form):
        blog = form.save(commit=False)
        blog.author = self.request.user
        blog.save()

        tags = form.cleaned_data.get('tags')
        if tags:
            tag_list = [tag.strip() for tag in tags.split(',') if tag.strip()]
            for tag in tag_list:
                BlogTag.objects.create(
                    name=tag,
                    blog=blog
                )

        return super().form_valid(form)


class UpdateBlog(UpdateView):
    model = Blog
    template_name = 'update-blog.html'
    success_url = reverse_lazy('blog:blog-detail')
    form_class = CreateBlogForm

    def form_valid(self, form):
        blog = form.save(commit=False)
        blog.author = self.request.user
        blog.save()

        tags = form.cleaned_data.get('tags')
        if tags:
            tag_list = [tag.strip() for tag in tags.split(',') if tag.strip()]
            for tag in tag_list:
                BlogTag.objects.create(
                    name=tag,
                    blog=blog
                )

        return super().form_valid(form)


class DeleteBlog(DeleteView):
    model = Blog
    template_name = 'delete-blog.html'
    success_url = reverse_lazy('blog:blog')
