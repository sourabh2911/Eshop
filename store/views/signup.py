from django.shortcuts import render, redirect
from django.views import View
from store.models.customer import Customer
from django.contrib.auth.hashers import make_password, check_password


class SignUp(View):
    def get(self, request):
        return render(request, 'signup.html')

    def post(self, request):
        postData = request.POST
        first_name = postData.get('firstname')
        last_name = postData.get('lastname')
        phone = postData.get('phone')
        email = postData.get('email')
        password = postData.get('password')

        values = {
            'first_name': first_name,
            'last_name': last_name,
            'phone': phone,
            'email': email
        }

        # data to be saved in database using object
        customer = Customer(first_name=first_name,
                            last_name=last_name,
                            phone=phone,
                            email=email,
                            password=password
                            )

        error_message = None
        error_message = self.validateCustomer(customer)

        # Form Submit
        if not error_message:
            customer.password = make_password(customer.password)
            customer.register()
            return redirect('homepage')
        else:
            data = {
                'error': error_message,
                'values': values
            }
            return render(request, 'signup.html', data)

    def validateCustomer(self, customer):
        error_message = None

        if not customer.first_name:
            error_message = "First Name Required!!"
        elif len(customer.first_name) < 3:
            error_message = "First Name length should be 2 or long"
        elif not customer.last_name:
            error_message = "Last Name Required!!"
        elif len(customer.last_name) < 4:
            error_message = "Last Name length should be 4 or long"
        elif not customer.phone:
            error_message = "Phone number Required!!"
        elif len(customer.phone) != 10:
            error_message = "Phone number should be 10 digit"
        elif not customer.email:
            error_message = "Email Required!!"
        elif len(customer.email) < 8:
            error_message = "Email length should be greater than 8"
        elif not customer.password:
            error_message = "Password Required!!"
        elif len(customer.password) < 8:
            error_message = "Password length should be 8 or long"
        elif customer.isExists():
            error_message = "Email address already exists"

        return error_message
