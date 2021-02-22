from django.shortcuts import render
from store.models.category import Categorie
from store.models.products import Product


# Create your views here.

def index(request):
    products = None
    categories = Categorie.get_all_categories()
    categoryID = request.GET.get('category')
    if categoryID:
        products = Product.get_all_products_by_category_id(categoryID)
    else:
        products = Product.get_all_products()

    data = {}
    data['products'] = products
    data['categories'] = categories

    print('You are : ', request.session.get('email'))
    return render(request, 'index.html', data)


# To validate user data & called from registerUser()





