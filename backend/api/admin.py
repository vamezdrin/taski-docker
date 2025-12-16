"""Досктринг можудя admin."""
from django.contrib import admin

from .models import Task


class TaskAdmin(admin.ModelAdmin):
    """Регистрайия задачи в админ панели."""

    list_display = ('title', 'description', 'completed')


admin.site.register(Task, TaskAdmin)
