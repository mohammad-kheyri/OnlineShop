from rest_framework.routers import DefaultRouter
from .views import BlogViewSet, BlogDetailViewSet
from django.urls import path, include

app_name = 'blog'

routers = DefaultRouter()
routers.register(r'blogs', BlogViewSet, basename='blogs')

routers.register(r'blogs-detail', BlogDetailViewSet, basename='blog-detail')

urlpatterns = [
    path("", include(routers.urls)), 
    path("<int:pk>/", include(routers.urls))
]