from django.db import models

from course.models import Course
from lesson.models import Lesson
from users.models import User

NULLABLE = {'null': True, 'blank': True}


class Payments(models.Model):
    """Модель для определения платежей пользователя"""

    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='пользователь')
    payment_date = models.DateField(verbose_name='дата оплаты', auto_now_add=True),
    payed_course = models.ForeignKey(Course, on_delete=models.CASCADE, **NULLABLE),
    payed_lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, **NULLABLE),
    payment_url = models.TextField(**NULLABLE, verbose_name='URL оплаты'),
    session_id = models.CharField(max_length=255, verbose_name="ID сессии", **NULLABLE)
    payment_sum = models.FloatField(verbose_name="Сумма платежа", default=1000)
    payment_type = models.CharField(
        verbose_name="Тип оплаты",
        choices=(("CASH", "Наличные"), ("CARD", "Перевод")),
        max_length=5,
        default="CASH"
    )

    class Meta:
        """Класс для корректного отображения в админке"""

        verbose_name = "Оплата пользователя"
        verbose_name_plural = "Оплаты пользователя"
