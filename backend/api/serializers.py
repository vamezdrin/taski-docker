"""Сериализатор для задач."""
from rest_framework import serializers

from .models import Task


class TaskSerializer(serializers.ModelSerializer):
    """Сериализатор для задач."""

    class Meta:
        """Мета класс."""

        model = Task
        fields = ('id', 'title', 'description', 'completed')
