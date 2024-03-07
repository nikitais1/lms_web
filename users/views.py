from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, generics
from rest_framework.filters import OrderingFilter

from users.models import User, Payment
from users.serializers import UserSerializer, PaymentsSerializer


class UserViewSet(viewsets.ModelViewSet):
    """Класс для просмотра пользователей"""
    serializer_class = UserSerializer
    queryset = User.objects.all()


class UserRetrieveView(generics.RetrieveAPIView):
    """Класс для просмотра пользователя"""
    serializer_class = UserSerializer


class UserUpdateView(generics.UpdateAPIView):
    """Класс для обновления пользователя"""
    serializer_class = UserSerializer
    queryset = User.objects.all()


class UserListView(generics.ListAPIView):
    """Класс для просмотра пользователя"""
    serializer_class = UserSerializer
    queryset = User.objects.all()


class UserDestroyView(generics.DestroyAPIView):
    """Класс для удаления пользователя"""
    serializer_class = UserSerializer
    queryset = User.objects.all()


class PaymentListAPIView(generics.ListAPIView):
    """Класс для просмотра списка платежей"""
    serializer_class = PaymentsSerializer
    queryset = Payment.objects.all()
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ('paid_course', 'paid_lesson', 'payment_method')
    ordering_fields = ('payments_date',)
