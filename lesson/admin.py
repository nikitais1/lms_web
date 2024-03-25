from django.contrib import admin

from lesson.models import Lesson


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    """Отображение списка уроков"""
    list_display = ('title', 'description', 'preview', 'course')

