from django.urls import path
from .views import BlogView, BlogDetailsView

app_name = "blog"

urlpatterns = [
    path('blog/', BlogView.as_view(), name='blog'),
    path('blog/<int:pk>/', BlogDetailsView.as_view(), name='blog-detail')
]
