from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.filters import OrderingFilter
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from course.models import Course
from course.serializers import CourseSerializer


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
