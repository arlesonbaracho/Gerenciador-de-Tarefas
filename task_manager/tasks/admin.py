from django.contrib import admin

# Register your models here.

from .models import Task

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_completed', 'due_date', 'user')
    list_filter = ('is_completed', 'due_date', 'category')
    search_fields = ('title', 'description', 'category')
