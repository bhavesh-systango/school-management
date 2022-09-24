import datetime
from django.http import HttpResponseNotFound
from django.shortcuts import redirect, render
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView
import stripe
from django.contrib.auth.mixins import LoginRequiredMixin
from django.conf import settings
from .models import Payment
from authentication.models import CustomUser
from django.http import JsonResponse
import json
import stripe
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

# This is your test secret API key.
stripe.api_key = 'sk_test_51LLhphSFpOmlnCCKZB3CPXzdTFXASapcJ9UnGZ7LVlbVvqpEZGGIAy6QKV2gozPvHpxBO0YnziiHLe4fbAmw3XqC00MJHbnHvn'


@method_decorator(csrf_exempt, name = 'dispatch')
class CreatePayment(TemplateView):
    
    def post(self, request):

        # try:    
        data = json.loads(request.body.decode("UTF-8"))
        print(data)
        print("*********************")
        # Create a PaymentIntent with the order amount and currency

        data_id = int(data['items'][0]['id'])
        print(type(data_id))
        print(data_id)

        payment_user = Payment.objects.select_related('user').filter(user_id  = data_id, status = 1, user__user_type = 1, paid_date__month = datetime.datetime.now().month)
        amount_to_pay = Payment.objects.filter( user = data_id, ).first()
        print(amount_to_pay)
        print(payment_user)
        
        intent = stripe.PaymentIntent.create(

            amount = ((amount_to_pay.amount) * 100), 
            currency = 'inr',
            automatic_payment_methods = {

                'enabled': True,
            },
        )

        print(intent['client_secret'])
        print(intent)

        return JsonResponse({

            'clientSecret' : intent['client_secret']
        })
        
        # except Exception as e :

        #     return JsonResponse(error=str(e)), 403


class PaymentFailure(LoginRequiredMixin,TemplateView):

    login_url = '/authentication/login/'
    template_name = "payment/payment_failure.html"
    

class PaymentSuccess(LoginRequiredMixin,TemplateView):

    login_url = '/authentication/login/'
    template_name = "payment/payment_success.html"

    def get(self, request):

        # , paid_date__month = 7
        student_pay = Payment.objects.filter(user = request.user , type = 1, paid_date__month =datetime.datetime.now().month, paid_date__year = datetime.datetime.now().year )

        print(student_pay)
        print("************ line90")

        if student_pay:

            print("!!!!!!!!!!")
 
            student_pay.status = 1
            student_pay.save()
            print(student_pay)

            return render(request,"payment/payment_success.html", {'context': student_pay })

        return render(request,"payment/payment_success.html")


class paymentView(LoginRequiredMixin, TemplateView):
    
    login_url = '/authentication/login/'
    template_name = 'payment/payment_details.html' 
    payslip = Payment.objects.all()
    user = CustomUser.objects.all()

    extra_context = {

        'payslip' : payslip,
        'user' : user
    }


class PaymentCard(LoginRequiredMixin, TemplateView):

    login_url = '/authentication/login/'
    template_name = 'payment/payment_card.html'
    queryset = Payment.objects.all()
    # fields = ["amount"]

    stripe.api_key = settings.STRIPE_SECRET_KEY     

    def get(self, request):

        print("---------------")
        context = {}
        context['key'] = settings.STRIPE_PUBLISHED_KEY
        context['student'] = request.user
        context['amount'] = Payment.objects.values_list('amount').filter(user = request.user) 
        context['month_year'] = Payment.objects.filter( paid_date__month = datetime.datetime.now().month, paid_date__year = datetime.datetime.now().year, status = 1 )
        return render(request, "payment/payment_card.html", context)


