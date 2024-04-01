from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from course.models import Course
from users.models import User


class SubcriptionTests(APITestCase):
    """Test на подписку"""
    def setUp(self):
        self.user = User.objects.create(email="testcase_user@thisistest.test", password="simple_password!")
        self.course = Course.objects.create('title', description='Test description', owner=self.user)

    def test_add_subscription(self):
        """Проверка создания подписки"""
        self.client.force_authenticate(user=self.user)
        data = {'user': self.user.id, 'course': self.course.id}
        response = self.client.post(
            reverse('course:subscription'), data=data
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            response.json(), {'message': 'Подписка добавлена'}
        )

    def test_destroy_subscription(self):
        """Проверка удаления подписки"""
        self.client.force_authenticate(user=self.user)
        data = {'user': self.user.id, 'course': self.course.id}
        self.client.post(
            reverse('course:subscription'), data=data
        )
        delete_response = self.client.post(
            reverse('course:subscription'), data=data
        )
        self.assertEqual(delete_response.status_code, status.HTTP_200_OK)

