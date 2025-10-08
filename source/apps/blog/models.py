from django.db import models
from apps.user.models import User



class BlogCategory(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class Blog(models.Model):
    title = models.CharField(max_length=100)
    body = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(BlogCategory, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class BlogComment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.blog

class BlogTag(models.Model):
    name = models.CharField(max_length=100)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class BlogReview(models.Model):
    name = models.CharField(max_length=100)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
