from rest_framework import serializers

from lesson.models import Lesson


class LessonSerializer(serializers.ModelSerializer):
    """Сериализатор для модели Уроков"""

    class Meta:
        """Вложенный класс для корректной работы сериализатора"""
        model = Lesson
        fields = "__all__"

    def create(self, validated_data):
        """Автоматическое добавление пользователя в созданный экземпляр класса"""
        user = self.context['request'].user
        lesson = Lesson(**validated_data)
        lesson.owner = user
        lesson.save()
        return lesson