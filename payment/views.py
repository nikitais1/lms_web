from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response

from course.models import Course
from .models import Payments
from .services_payment import StripePayment


# Create your views here.

class PaymentAPIView(APIView):
    """Класс для возможности совершать платежи"""

    def post(self, *args, **kwargs):
        # sourcery skip: extract-method, remove-unnecessary-else, use-named-expression
        course_id = self.request.data["course"]
        course_item = get_object_or_404(Course, pk=course_id)
        if course_item:
            payment_class = StripePayment()

            product_id = payment_class.create_product(name="Оплата курса", description="Оплата курса")
            price_id = payment_class.create_price(amount=10000, product_id=product_id, currency="rub")
            payment_url, session_id = payment_class.create_session(price_id=price_id)

            new_payment = Payments.objects.create(
                user=self.request.user,
                payment_url=payment_url,
                payed_course=course_item,
                session_id=session_id
            )
            new_payment.save()
            return Response({"message": "Ссылка для оплаты", "url": payment_url})
        else:
            print("Такого курса нет")
            return Response({"message": "Нет такого курса"})