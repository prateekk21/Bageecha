from django.shortcuts import render
from .models import Product
# from category.models import Category

# Create your views here.
def store(request, category_slug = None):

    if category_slug!=None:
        products = Product.objects.all().filter(category__slug = category_slug, is_available=True)

    else:
        products = Product.objects.all().filter(is_available = True)
    
    product_count = products.count()
    context = {
        'products' : products,
        'product_count': product_count,
    }
    return render(request, 'store/store.html', context)

def product_detail(request, category_slug, product_slug):

    try:
        single_product = Product.objects.get(slug = product_slug, category__slug = category_slug)

    except Exception as e:
        raise e

    context = {
        'single_product':single_product,
    }
    return render(request, 'store/product_detail.html',context)