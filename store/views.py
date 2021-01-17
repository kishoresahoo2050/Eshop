from django.shortcuts import render
from .models.products import Products
from .models.category import Category
from .models.customer import Customer
from django.contrib import messages
import re
# Create your views here.


def index(request):
    category_id = request.GET.get('category')
    if category_id:
        all_prod = Products.get_category_by_products(category_id)
    else:
        all_prod = Products.get_all_products()
    all_cate = Category.get_all_cate()
    context = {"all_cate": all_cate,
               "all_prod": all_prod, "category_id": category_id}
    return render(request, 'store/index.htm', context)


def signup(request):
    errors = {}
    form   = {}
    email_regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
    if request.method == 'POST':
        name     = request.POST.get('name')
        email    = request.POST.get('email')
        pnum     = request.POST.get('pnum')
        password = request.POST.get('password')

        form['name']     = name
        form['email']    = email
        form['pnum']     = pnum
        form['password'] = password
        

        if not name:
            errors['name'] = "Name Fields Must Be Required*"
        if not email:
            errors['email'] = "Email Fields Must Be Required*"
        if not pnum:
            errors['pnum'] = "Phone Fields Must Be Required*"
        if not password:
            errors['password'] = "Password Fields Must Be Required *"
        if len(pnum)!=0 and len(pnum)!=10:
            errors['pnum'] = "Phone Number Fields Only Contain 10 Digit"
        if len(email)!=0 and not re.search(email_regex,email):
             errors['email'] = "Email Pattern Is not macthed ."
        if re.search(email_regex,email):
            count_email = Customer.objects.filter(email=email).count()
            if count_email!=0:
                errors['email'] = "Email Id Already Exist."

        if len(pnum)==10:
            count_phone = Customer.objects.filter(phone=pnum).count()
            if count_phone!=0:
                errors['pnum'] = "Phone Number Already Exist."

        if not errors:
            insertCustomer = Customer(name=name,email=email,phone=pnum,password = password)
            insertCustomer.save()
            messages.success(request,'Account Create Successfully.')
            form = {}
        

    return render(request, 'store/signup.htm', {"errors": errors,"form":form})
