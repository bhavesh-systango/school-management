from django.urls import path
from .views import PaymentFailure, PaymentSuccess,PaymentCard,CreatePayment

app_name = "payment"

urlpatterns = [

    path('paymentfailure/',PaymentFailure.as_view(),name = "failure "),
    path('paymentsuccess/',PaymentSuccess.as_view(),name = "success"),
    # path('paymentgateway/',views.PaymentGateway.as_view(),name = "paymentgateway"),
    path('paymentcard/',PaymentCard.as_view(),name = "paymentcard"),
    path('createpayment/',CreatePayment.as_view(),name = "create_payment"),
    # path('paymentdetails/',PaymentForm.as_view(), name = "paymentdetails"),

]

