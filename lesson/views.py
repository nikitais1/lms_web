from rest_framework import generics

from lesson.models import Lesson
from lesson.serializers import LessonSerializer


class LessonCreateAPIView(generics.CreateAPIView):
    """Класс для создания урока"""
    serializer_class = LessonSerializer


class LessonUpdateAPIView(generics.UpdateAPIView):
    """Класс для обновления урока"""
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()


class LessonListAPIView(generics.ListAPIView):
    """Класс для просмотра списка уроков"""
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()


class LessonRetrieveAPIView(generics.RetrieveAPIView):
    """Класс для просмотра одного урока"""
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()


class LessonDestroyAPIView(generics.DestroyAPIView):
    """Класс для удаления урока"""
    queryset = Lesson.objects.all()

