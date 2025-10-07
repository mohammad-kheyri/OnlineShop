from django.contrib import admin

from .models import BlogCategory, Blog, BlogComment, BlogTag, BlogReview

@admin.register(BlogCategory)
class AdminBlogCategory(admin.ModelAdmin):
    pass


@admin.register(Blog)
class AdminBlig(admin.ModelAdmin):
    pass


@admin.register(BlogComment)
class AdminBlogComment(admin.ModelAdmin):
    pass


@admin.register(BlogTag)
class AdminBlogTag(admin.ModelAdmin):
    pass


@admin.register(BlogReview)
class AdminBlogReview(admin.ModelAdmin):
    pass
