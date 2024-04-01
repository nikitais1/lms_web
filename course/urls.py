from rest_framework.routers import DefaultRouter
from django.urls import path

from course.apps import CourseConfig
from course.views import CourseViewSet, SubscriptionAPIView

app_name = CourseConfig.name

router = DefaultRouter()
router.register(r'course', CourseViewSet, basename='course')
urlpatterns = [
    path('subscribe/', SubscriptionAPIView.as_view(), name='subscription')
] + router.urls
