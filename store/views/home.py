from django.shortcuts import render
from store.models.products import Products
from store.models.category import Category


def index(request):
    cart = request.session.get('cart')
    if not cart:
        request.session['cart'] = {}

    # request.session['cart'].clear()
    if request.method == 'POST':
        products_id = request.POST.get('product')
        remove_id    = request.POST.get('remove')
       
        if cart:
            qty = cart.get(products_id)
            if qty:
                if remove_id:
                    cart[products_id] = qty-1
                    if qty==1:
                        cart.pop(products_id)
                else:
                    cart[products_id] = qty+1
            else:
                cart[products_id] = 1
        else:
            cart[products_id] = 1
        request.session['cart'] = cart
        # print(cart)
    category_id = request.GET.get('category')
    if category_id:
        category_id = int(category_id)
    if category_id:
        all_prod = Products.get_category_by_products(category_id)
    else:
        all_prod = Products.get_all_products()
    all_cate = Category.get_all_cate()
    context = {"all_cate": all_cate,
               "all_prod": all_prod, "category_id": category_id}
    return render(request, 'store/index.htm', context)
