from rest_framework import serializers
from .models import BlogPost

class BlogPostSerializers(serializers.Serializers):
    title = serializers.CharField(max_length=255)
    content = serializers.CharField(max_length=1000)