from django.contrib import admin
from .models import Task


# Register your models here.
class TaskList(admin.ModelAdmin):
    list_display = ['id', 'title', 'date_to_do', 'check', 'timestamp']


admin.site.register(Task, TaskList)
