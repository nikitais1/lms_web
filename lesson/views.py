from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from rest_framework.filters import OrderingFilter
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from lesson.models import Lesson
from lesson.permissions import IsOwner
from lesson.serializers import LessonSerializer
from users.permissions import IsModerator


class LessonCreateAPIView(generics.CreateAPIView):
    """Класс для создания урока"""
    serializer_class = LessonSerializer
    permission_classes = [IsAuthenticated]
    queryset = Lesson.objects.all()


class LessonUpdateAPIView(generics.UpdateAPIView):
    """Класс для обновления урока"""
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsModerator, IsOwner]
    filter_backends = [DjangoFilterBackend, OrderingFilter]


class LessonListAPIView(generics.ListAPIView):
    """Класс для просмотра списка уроков"""
    serializer_class = LessonSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, OrderingFilter]

    def get_queryset(self):
        if self.request.user.groups.filter(name='moderators').exists():
            return Lesson.objects.all()
        return Lesson.objects.filter(owner=self.request.user)


class LessonRetrieveAPIView(generics.RetrieveAPIView):
    """Класс для просмотра одного урока"""
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsModerator, IsOwner]
    filter_backends = [DjangoFilterBackend, OrderingFilter]


class LessonDestroyAPIView(generics.DestroyAPIView):
    """Класс для удаления урока"""
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsAdminUser, IsOwner]
    filter_backends = [DjangoFilterBackend, OrderingFilter]

