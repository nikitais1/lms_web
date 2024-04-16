from django.contrib.auth.models import AbstractUser
from django.db import models


NULLABLE = {'null': True, 'blank': True}


class User(AbstractUser):
    username = None
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    email = models.EmailField(unique=True, verbose_name='почта')
    avatar = models.ImageField(upload_to='users/', **NULLABLE, verbose_name='аватар')
    phone = models.CharField(max_length=150, **NULLABLE, verbose_name='телефон')
    country = models.CharField(max_length=100, **NULLABLE, verbose_name='страна')
    temporary_password = models.CharField(verbose_name="Temporary password", max_length=6, **NULLABLE)
    is_moderator = models.BooleanField(verbose_name="Модератор?", default=False)
    last_login = models.DateTimeField(verbose_name="Последнее посещение сервиса", auto_now=True, **NULLABLE)

    def __str__(self):
        return f'{self.email} - {self.phone}'

    class Meta:
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'

