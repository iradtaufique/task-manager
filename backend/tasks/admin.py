from django.contrib import admin
from .models import Category, Task

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'color', 'created_at']
    search_fields = ['name']


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'status', 'completed', 'category', 'created_at']
    list_filter = ['status', 'completed', 'category']
    search_fields = ['title', 'desciption']
    list_editable = ['status', 'completed']
