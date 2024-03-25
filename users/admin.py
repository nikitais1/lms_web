from django.contrib import admin

from course.models import Course
from users.models import Payment, User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    """Отображение списка пользователей"""
    list_display = ('phone', 'email')


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    """Отображение списка платежей"""
    list_display = ('user', 'payments_date', 'paid_course', 'paid_lesson')


