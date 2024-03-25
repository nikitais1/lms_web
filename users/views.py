from rest_framework import generics
from rest_framework.filters import OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend

from rest_framework.permissions import IsAuthenticated, AllowAny

from .models import Payment, User
from .permissions import IsModerator
from .serializers import PaymentSerializer, UserSerializer


class PaymentsAPIListView(generics.ListAPIView):
    """Для показа всех данных о пользователе"""
    serializer_class = PaymentSerializer
    queryset = Payment.objects.all()
    permission_classes = [IsAuthenticated]

    filter_backends = (DjangoFilterBackend, OrderingFilter)
    filterset_fields = ("payed_course", "payed_lesson", "payment_type")
    ordering_fields = ("payment_date",)


class UserAPIListView(generics.ListAPIView):
    """Просмотр всех пользователей"""
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated]


class UserCreateAPIView(generics.CreateAPIView):
    """Создание пользователя"""
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [AllowAny]


class UserUpdateAPIView(generics.UpdateAPIView):
    """Изменение пользователя"""
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [IsModerator]


class UserDeleteAPIView(generics.DestroyAPIView):
    """Удаление пользователя"""
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [IsModerator]
