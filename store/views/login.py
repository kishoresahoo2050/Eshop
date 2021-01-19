from .universal_imp import render, Customer,redirect
from django.contrib.auth.hashers import check_password
from store.validation_handle import Customer_login
from django.core.exceptions import ObjectDoesNotExist
from django.views import View


class LoginUser(View):

    def __init__(self):
        self.errors = None
        self.form = {}

    def get(self, request):
        if not request.session.get('user_id'):
            return render(request, 'store/login.htm', {"errors": self.errors, "form": self.form})
        else:
           return  redirect('home')

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
                    request.session['user_id'] = get_user.id
                    request.session['user_name'] = get_user.name
                    return redirect('home')
                else:
                    self.errors['password'] = "Invalid Password"
            else:
                self.errors['email'] = "Invalid User Name"

        return render(request, 'store/login.htm', {"errors": self.errors, "form": self.form})



class Logout(View):

    def get(self,request):
        if request.session.get('user_id'):
            del request.session['user_id']
            del request.session['user_name']
        # print(request.session['user_id'])
        return redirect('login')
