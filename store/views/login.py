from .universal_imp import render, Customer
from django.contrib.auth.hashers import check_password
from store.validation_handle import Customer_login
from django.core.exceptions import ObjectDoesNotExist
from django.views import View


class LoginUser(View):

    def __init__(self):
        self.errors = None
        self.form = {}

    def get(self, request):

        return render(request, 'store/login.htm', {"errors": self.errors, "form": self.form})

    def post(self, request):
        email = request.POST.get('email')
        password = request.POST.get('password')

        self.form['email'] = email
        self.form['password'] = password

        self.errors = Customer_login(self.form)

        if not self.errors:
            try:
                get_user = Customer.objects.get(email=email)
            except ObjectDoesNotExist:
                get_user = False

            if get_user:
                if check_password(password, get_user.password):
                    print('run')
                else:
                    self.errors['password'] = "Invalid Password"
            else:
                self.errors['email'] = "Invalid User Name"

        return render(request, 'store/login.htm', {"errors": self.errors, "form": self.form})
