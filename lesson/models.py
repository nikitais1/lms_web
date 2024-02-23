from django.db import models

from course.models import Course

NULLABLE = {'null': True, 'blank': True}


class Lesson(models.Model):
    title = models.CharField(max_length=150, verbose_name='Название', **NULLABLE)
    preview = models.ImageField(upload_to='lesson/', **NULLABLE, verbose_name='Превью')
    description = models.TextField(verbose_name='Описание', **NULLABLE)
    link_to_video = models.URLField(verbose_name='Ссылка на видео', **NULLABLE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='Курс', **NULLABLE)

    class Meta:
        verbose_name = 'Урок'
        verbose_name_plural = 'Уроки'

    def __str__(self):
        return self.title
