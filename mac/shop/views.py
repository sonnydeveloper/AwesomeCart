from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
from math import ceil


# Create your index for single slider.
# def index(request):
#     products = Product.objects.all()
#     n = len(products)
#     nSlides = n // 4 + ceil((n / 4) - (n // 4))
#     params = {'no_of_slides': nSlides, 'range': range(1, nSlides), 'product': products}
#     return render(request, 'shop/index.html', params)

def index(request):
    allProds = []
    catProds = Product.objects.values('category', 'id')
    cats = {item['category'] for item in catProds}
    for cat in cats:
        prod = Product.objects.filter(category=cat)
        n = len(prod)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        allProds.append([prod, range(1, nSlides), nSlides])

    params = {'allProds': allProds}
    return render(request, 'shop/index.html', params)


def about(request):
    return render(request, 'shop/about.html')


def contact(request):
    return render(request, 'shop/contact.html')


def tracker(request):
    return render(request, 'shop/tracker.html')


def search(request):
    return render(request, 'shop/search.html')


def productView(request, myid):
    product = Product.objects.filter(id=myid)

    return render(request, 'shop/productview.html', {'product': product[0]})


def checkout(request):
    return render(request, 'shop/checkout.html')
