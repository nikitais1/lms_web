from rest_framework.routers import DefaultRouter
from django.urls import path
from users.apps import UsersConfig
from users.views import UserViewSet, UserRetrieveView, UserUpdateView, UserDestroyView, UserListView, PaymentListAPIView

app_name = UsersConfig.name


urlpatterns = [
    path('detail/<int:pk>/', UserRetrieveView.as_view(), name='user-detail'),
    path('update/<int:pk>/', UserUpdateView.as_view(), name='user-update'),
    path('delete/<int:pk>/', UserDestroyView.as_view(), name='user-delete'),
    path('users_list/', UserListView.as_view(), name='users_list'),
    path('payments/', PaymentListAPIView.as_view(), name='payments'),
]
