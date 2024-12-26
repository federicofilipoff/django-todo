from django.contrib import admin
from .models import Task

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'task', 'done', 'created_at', 'updated_at')
    list_filter = ('done',)
    search_fields = ('task',)
