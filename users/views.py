from rest_framework import generics

from rest_framework.permissions import IsAuthenticated, AllowAny

from .models import User
from .permissions import IsModerator
from .serializers import UserSerializer


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
