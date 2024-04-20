from django.shortcuts import render
from goodsapp.models import Products


def catalog(request):
    goods = Products.objects.all()

    context = {
        "title": "SportHub - Каталог",
        "goods": goods,
        # "slug_url": category_slug
    }
    return render(request, 'goodsapp/catalog.html', context)
    

def product(request):
    product = Products.objects.get(slug=product_slug)

    context = {
        'product': product
    }

    return render(request, 'goodsapp/product.html', context)

