from django.urls import path
from users.apps import UsersConfig
from users.views import PaymentsAPIListView, UserCreateAPIView, UserAPIListView, UserDeleteAPIView, UserUpdateAPIView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


app_name = UsersConfig.name


urlpatterns = [
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('create/', UserCreateAPIView.as_view(), name='users-create'),
    path('update/<int:pk>/', UserUpdateAPIView.as_view(), name='user-update'),
    path('delete/<int:pk>/', UserDeleteAPIView.as_view(), name='user-delete'),
    path('users_list/', UserAPIListView.as_view(), name='users_list'),
    path('payments/', PaymentsAPIListView.as_view(), name='payments'),
]
