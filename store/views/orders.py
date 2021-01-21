from .universal_imp import render,redirect
from store.models import Orders

def All_Orders(request):
    user_id = request.session.get('user_id')
    all_orders = Orders.objects.filter(customer = user_id).order_by('-id')
    # print(Cart_products)
    return render(request,'store/orders.htm',{"All_orders":all_orders})
