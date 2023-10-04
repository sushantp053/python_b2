from django.shortcuts import render
from django.http import HttpResponse

from product.models import Product

# Create your views here.


def product(request):
    q = Product.objects.all().values()
    print(q)

    return render(request, "prod.html", context={"product": q})
