from django.urls import path
from .views import BlogView, BlogDetailsView, CreateBlog, UpdateBlog, DeleteBlog

app_name = "blog"

urlpatterns = [
    path('blog/', BlogView.as_view(), name='blog'),
    path('blog/<int:pk>/', BlogDetailsView.as_view(), name='blog-detail'),
    path('create-blog/', CreateBlog.as_view(), name='create-blog'),
    path('update-blog/<int:pk>/', UpdateBlog.as_view(), name='update-blog'),
    path('delete-blog/<int:pk>/', DeleteBlog.as_view(), name='delete-blog')
]
