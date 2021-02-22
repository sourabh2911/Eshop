from django.shortcuts import render, redirect
from django.views import View
from store.models.customer import Customer
from django.contrib.auth.hashers import check_password


class Login(View):
    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
        email = request.POST.get('email')
        password = request.POST.get('password')
        customerData = Customer.get_customer_by_email(email)

        error_message = None
        print(customerData)
        print(email, password)

        if not email:
            error_message = "Email address required!!"
        elif len(email) < 10:
            error_message = "Email length should be greater than 8"
        elif not password:
            error_message = "Password Required!!"
        elif len(password) < 8:
            error_message = "Password length should be 8 or long"
        elif customerData and check_password(password, customerData.password):
            request.session['customer_id'] = customerData.id
            request.session['email'] = customerData.email

            return redirect('homepage')
            '''flag = check_password(password, customerData.password)
            if flag:
                return render('homepage')
            else:
                error_message = "Invalid email or password!!"'''
        else:
            error_message = "Invalid email or password!!"

        data = {
            'email': email,
            'error': error_message
        }

        return render(request, 'login.html', data)