from .universal_imp import render,redirect
from store.models import Products

def Cart(request):
    if request.session.get('user_id'):
        prod_id = list(request.session.get('cart'))
        if prod_id:
            Cart_products = Products.objects.filter(id__in = prod_id)
        else:
            Cart_products = None
        # print(Cart_products)
        return render(request,'store/cart.htm',{"All_prodcuts":Cart_products})
    else:
        return redirect('login')
