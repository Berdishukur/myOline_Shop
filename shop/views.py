from django.shortcuts import render, get_object_or_404
from .models import Category,Product
from cart.forms import CartAddProductFrom


def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.filter(category=category)

    context = {
        'category': category,
        'categories': categories,
        'products': products
    }
    return render(request, 'shop/product/list.html', context)

def product_detail(request,id , slug):
    product=get_object_or_404(Product,id=id,slug=slug,available=True)
    cart_product_from=CartAddProductFrom()
    return render(request,
                  'shop/product/detail.html',
                  {'producr':product,
                    'cart_product_from':cart_product_from})



