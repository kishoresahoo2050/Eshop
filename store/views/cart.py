from .universal_imp import render,redirect
from store.models import Products,Orders

def Cart(request):
    
    if request.session.get('user_id'):
        cart = request.session.get('cart')
        
        prod_id = list(cart)
        if prod_id:
            Cart_products = Products.objects.filter(id__in = prod_id)
        else:
            Cart_products = None
        
        if request.method == 'POST':
            phone   = request.POST.get('pnum')
            address = request.POST.get('address')
            user_id = request.session['user_id']
            # print(phone,address,Cart_products,user_id)
            for product in Cart_products:
                order = Orders(
                    product_id = product.id,
                    customer_id = user_id,
                    qty         = int(cart.get(str(product.id))),
                    price       = product.price,
                    address     = address,
                    phone       = phone
                    )
                order.save()
            request.session['cart'] = {}
            return redirect('cart')
        # print(Cart_products)
        return render(request,'store/cart.htm',{"All_prodcuts":Cart_products})
    else:
        return redirect('login')
