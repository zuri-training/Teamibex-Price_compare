from django.shortcuts import render
from products.models import Product
# Create your views here.


def search_venues(request):
    if request.method == "POST":
        searched = request.POST['searched']
        products = Product.objects.filter(name__contains=searched)
        return render(request, 'search_venues.html', {'searched': searched, 'products': products})
    else:
        return render(request, 'search_venues.html', {'searched': searched, 'products': products})
