from django.urls import path
from .views import BlogView, BlogDetailsView

urlpatterns = [
    path('blog/', BlogView.as_view(), name='blog'),
    path('blog/<int:pk>/', BlogDetailsView.as_view(), name='blog-detail')
]
