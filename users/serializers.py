from rest_framework import serializers

from users.models import User, Payment


class UserSerializer(serializers.ModelSerializer):
    """Класс сериализатора для пользователя"""
    class Meta:
        model = User
        fields = '__all__'


class PaymentsSerializer(serializers.ModelSerializer):
    """Класс сериализатора для платежей"""
    class Meta:
        model = Payment
        fields = '__all__'
