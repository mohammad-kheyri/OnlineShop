from django.contrib import admin

from .models import BlogCategory, Blog, BlogComment, BlogTag, BlogReview


@admin.register(BlogCategory)
class AdminBlogCategory(admin.ModelAdmin):
    search_fields = ['name']


class AdminBlogTag(admin.TabularInline):
    model = BlogTag

@admin.register(Blog)
class AdminBlog(admin.ModelAdmin):
    list_display = ('title', 'author', 'category')
    search_fields = ('name',)
    list_filter = ('category',)
    inlines = [AdminBlogTag]

    autocomplete_fields = ('category',)

@admin.register(BlogComment)
class AdminBlogComment(admin.ModelAdmin):
    search_fields = ['name']


@admin.register(BlogReview)
class AdminBlogReview(admin.ModelAdmin):
    search_fields = ['name']
