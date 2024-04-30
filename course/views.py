from django.core.mail import send_mail
from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, status
from rest_framework.filters import OrderingFilter
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView

from config import settings
from course.models import Course, CourseSubscribe
from course.serializers import CourseSerializer
from users.models import User
from course.signals import handle_course_save


class CourseViewSet(viewsets.ModelViewSet):
    """Класс для просмотра списка курсов"""
    serializer_class = CourseSerializer
    queryset = Course.objects.all()
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, OrderingFilter]

    def get_permissions(self):
        if self.action == 'create' or self.action == 'update' or self.action == 'partial_update' or self.action == 'destroy':
            return [IsAdminUser()]
        return super().get_permissions()

    def get_queryset(self):
        qs = Course.objects.all()
        if not self.request.user.is_moderator:
            qs = qs.owner(self.request.user)
        return qs

    def perform_create(self, serializer):
        """Автоматическое добавление пользователя в новый экземпляр класса"""
        serializer.save(owner=self.request.user)

    def perform_update(self, serializer):
        """Метод для запуска функции отправки уведомлений об обновлении курса"""
        update_course = serializer.save()
        handle_course_save.delay(update_course.id)
        update_course.save()


class SubscriptionAPIView(APIView):
    """Механизм для смены флага подписки на курс"""

    def post(self, request, *args, **kwargs):
        """Реализация задания через post метод"""
        user = request.user
        course_id = request.data.get("course")
        course_item = get_object_or_404(Course, pk=course_id)

        subs_item = CourseSubscribe.objects.filter(user=user, course=course_item)

        if subs_item.exists():
            subs_item.delete()
            message = "Подписка удалена"
        else:
            CourseSubscribe.objects.create(user=user, course=course_item)
            message = "Подписка добавлена"

        return Response({"message": message}, status=status.HTTP_200_OK)
