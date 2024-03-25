from rest_framework import serializers

from users.models import User, Payment


class UserSerializer(serializers.ModelSerializer):
    """Класс сериализатора для пользователя"""
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = "__all__"

    def create(self, validated_data):
        """Метод для хеширования сырого пароля"""

        password = validated_data.pop("password")
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user


class PaymentSerializer(serializers.ModelSerializer):
    """Класс сериализатора для платежей"""

    class Meta:
        model = Payment
        fields = '__all__'
