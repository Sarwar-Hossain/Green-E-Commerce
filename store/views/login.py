from django.shortcuts import render, redirect
from django.contrib.auth.hashers import check_password
from store.models.customer import Customer
from django.views import View
from django.contrib.sessions.models import Session


class Login(View):
    @staticmethod
    def get(self, request):
        return render(request, 'login.html')

    @staticmethod
    def post(self, request):
        email = request.POST.get('email')
        password = request.POST.get('password')
        customer = Customer.get_user_by_email(email)
        error_message = None
        if customer:
            flag = check_password(password, customer.password)
            if flag:
                request.session['customer_id'] = customer.id
                request.session['email'] = customer.email
                return redirect('homepage')
            else:
                error_message = "Email address or password is incorrect"
        else:
            error_message = "Email address or password is incorrect"
        return render(request, "login.html", {'error': error_message})

