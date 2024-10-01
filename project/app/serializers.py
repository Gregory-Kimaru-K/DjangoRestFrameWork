from rest_framework import serializers
from .models import Task

class TaskSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=255)
    content = serializers.CharField(style={'base_template' : 'textarea.html'})
    slug = serializers.CharField(read_only=True)

    def create(self, validated_data):
        return Task.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        self.title = validated_data.get('title', instance.title)
        self.content = validated_data.get('content', instance.content)
        instance.save()
        return instance