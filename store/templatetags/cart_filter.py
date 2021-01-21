from django import template

register = template.Library()

@register.filter(name='is_in_cart')
def is_in_cart(product,cart):
    for c_key in cart:
       if int(c_key) == product:
           return True
    return False


@register.filter(name='cart_count')
def cart_count(product,cart):
    for c_key in cart:
        if int(c_key) == product:
            return cart.get(c_key)
    return 0


@register.filter(name="count_cart")
def count_cart(prod):
    return sum(prod)


@register.filter(name="Cart_price")
def Product_cart_price(product,cart):
    return product.price*cart_count(product.id,cart)

@register.filter(name="Total_price")
def Total_price(all_product,cart):
    total = 0
    for products in all_product:
        total +=Product_cart_price(products,cart)
    return total


@register.filter(name = 'multiply')
def Multily_num(qty,price):
    return qty*price
    

    



