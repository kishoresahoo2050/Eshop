from .universal_imp import render, Customer, messages
from django.contrib.auth.hashers import make_password
from store.validation_handle import Customer_Valid


def signup(request):
    errors = None
    form = {}

    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        pnum = request.POST.get('pnum')
        password = request.POST.get('password')

        form['name'] = name
        form['email'] = email
        form['pnum'] = pnum
        form['password'] = password

        errors = Customer_Valid(form)
        if not errors:
            password = make_password(password)
            insertCustomer = Customer(
                name=name, email=email, phone=pnum, password=password)
            insertCustomer.save()
            messages.success(request, 'Account Create Successfully.')
            form = {}

    return render(request, 'store/signup.htm', {"errors": errors, "form": form})
