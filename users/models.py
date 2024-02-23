from django.contrib.auth.models import AbstractUser
from django.db import models

NULLABLE = {'null': True, 'blank': True}


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name='почта')

    avatar = models.ImageField(upload_to='users/', **NULLABLE, verbose_name='аватар')
    phone = models.CharField(max_length=150, **NULLABLE, verbose_name='телефон')
    country = models.CharField(max_length=100, **NULLABLE, verbose_name='страна')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

