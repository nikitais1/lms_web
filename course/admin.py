from django.contrib import admin

from course.models import Course


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    """Отображение списка курсов"""
    list_display = ('title', 'preview', 'description')

