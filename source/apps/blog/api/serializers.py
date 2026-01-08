from rest_framework import serializers
from apps.blog.models import Blog

class BlogSerializers(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields =  ['id', 'title']


class BlogDetailSerializers(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = '__all__'
        