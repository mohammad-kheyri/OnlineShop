from django.db import models
from apps.user.models import User
from ckeditor.fields import RichTextField


class BlogCategory(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class Blog(models.Model):
    title = models.CharField(max_length=100)
    body = RichTextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(BlogCategory, on_delete=models.CASCADE)
    image = models.ImageField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class BlogComment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    body = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.body

class BlogTag(models.Model):
    name = models.CharField(max_length=100)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class BlogReview(models.Model):
    name = models.CharField(max_length=100)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    body = models.TextField(null=True)

    def __str__(self):
        return self.name
    
