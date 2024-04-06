from django.urls import path
from payment import views
from payment.apps import PaymentConfig

# Название этого приложения
app_name = PaymentConfig.name

urlpatterns = [
    path("pay/", views.PaymentAPIView.as_view(), name="payment"),
]