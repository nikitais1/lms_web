from rest_framework import serializers

from course.models import Course, CourseSubscribe
from lesson.models import Lesson


class CourseSerializer(serializers.ModelSerializer):
    num_lessons = serializers.SerializerMethodField()
    lesson_list = serializers.SerializerMethodField()
    is_subscribed = serializers.SerializerMethodField()

    class Meta:
        model = Course
        fields = '__all__'

    def get_is_subscribed(self, obj):
        user = self.context['request'].user
        if user.is_authenticated:
            return CourseSubscribe.objects.filter(user=user, course=obj).exists()
        return False

    def get_num_lessons(self, course):
        return Lesson.objects.filter(course=course).count()

    def get_lesson_list(self, course):
        """Метод для вывода списка уроков, входящих в курс"""
        return [lesson.lesson_name for lesson in Lesson.objects.filter(course=course)]

    def create(self, validated_data):
        """Автоматическое добавление пользователя в созданный экземпляр класса"""
        user = self.context['request'].user
        print(user)
        course = Course(**validated_data)
        course.owner = user
        course.save()
        return course


class SubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseSubscribe
        fields = '__all__'
