from django.shortcuts import render
from store.models.products import Products
from store.models.category import Category


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
