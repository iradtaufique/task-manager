from rest_framework import serializers
from .models import Category, Task

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model  = Category
        fields = ['id', 'name', 'color', 'created_at']
        read_only_fields = ['id', 'created_at']

class TaskSerializer(serializers.ModelSerializer):
    category_details = CategorySerializer(
        source="category",
        read_only=True
    )
    class Meta:
        model = Task
        fields = [
            'id',
            'title',
            'description',
            'status',
            'completed',
            'category',          # accepts category id on write
            'category_details',   # returns full category object on read
            'created_at',
            'updated_at',
        ]
        read_only_fields = ['id', 'created_at', 'updated_at']