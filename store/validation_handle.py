from .models.customer import Customer
import re

def Customer_Valid(Customers):
    errors = {}
    email_regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
    name     = Customers.get('name')
    email    = Customers.get('email')
    pnum     = Customers.get('pnum')
    password = Customers.get('password')


    if not name:
        errors['name'] = "Name Fields Must Be Required*"
    if not email:
        errors['email'] = "Email Fields Must Be Required*"
    if not pnum:
        errors['pnum'] = "Phone Fields Must Be Required*"
    if not password:
        errors['password'] = "Password Fields Must Be Required *"
    if pnum and len(pnum)!=10:
        errors['pnum'] = "Phone Number Fields Only Contain 10 Digit"
    if len(email)!=0 and not re.search(email_regex,email):
        errors['email'] = "Email Pattern Is not macthed ."
    if re.search(email_regex,email):
        count_email = Customer.objects.filter(email=email).count()
        if count_email!=0:
            errors['email'] = "Email Id Already Exist."

    if pnum and len(pnum)==10:
        count_phone = Customer.objects.filter(phone=pnum).count()
        if count_phone!=0:
            errors['pnum'] = "Phone Number Already Exist."
        
    return errors


def Customer_login(Customers):
    errors = {}
    email_regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
    email    = Customers.get('email')
    password = Customers.get('password')

    if not email:
        errors['email'] = "Email Fields Must Be Required*"

    if not password:
        errors['password'] = "Password Fields Must Be Required *"

    if len(email)!=0 and not re.search(email_regex,email):
        errors['email'] = "Email Pattern Is not macthed ."
    

    return errors





































































