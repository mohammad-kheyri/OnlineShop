from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .serializers import BlogSerializers, BlogDetailSerializers

from apps.blog.models import Blog


class BlogViewSet(viewsets.ModelViewSet):

    queryset = Blog.objects.all()   
    serializer_class = BlogSerializers
    permission_classes = [IsAuthenticated]
    

class BlogDetailViewSet(viewsets.ModelViewSet):
    
    queryset = Blog.objects.all()
    serializer_class = BlogDetailSerializers
    permission_classes = [IsAuthenticated]