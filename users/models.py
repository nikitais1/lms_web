from django.contrib.auth.models import AbstractUser
from django.db import models

from course.models import Course
from lesson.models import Lesson

NULLABLE = {'null': True, 'blank': True}


class User(AbstractUser):
    username = None
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    email = models.EmailField(unique=True, verbose_name='почта')
    avatar = models.ImageField(upload_to='users/', **NULLABLE, verbose_name='аватар')
    phone = models.CharField(max_length=150, **NULLABLE, verbose_name='телефон')
    country = models.CharField(max_length=100, **NULLABLE, verbose_name='страна')

    def __str__(self):
        return f'{self.email} - {self.phone}'

    class Meta:
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'


class Payment(models.Model):
    PAYMENT_METHOD_CHOICES = [
        ('cash', 'наличные'),
        ('card', 'банковский перевод')
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='пользователь')
    payments_date = models.DateTimeField(auto_now=True, verbose_name='дата оплаты')
    paid_course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='оплаченный курс', **NULLABLE)
    paid_lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, verbose_name='оплаченный урок', **NULLABLE)
    payment_sum = models.PositiveIntegerField(verbose_name='сумма платежа')
    payment_method = models.CharField(max_length=50, verbose_name='способ оплаты')

    def __str__(self):
        return (f'{self.user}: {self.paid_course} {self.paid_lesson}'
                f'{self.payment_sum} {self.payment_method} {self.payments_date}')

    class Meta:
        verbose_name = 'платеж'
        verbose_name_plural = 'платежи'
        ordering = ['-payments_date']
