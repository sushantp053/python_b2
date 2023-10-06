from django.shortcuts import render
from django.http import HttpResponse

from product.models import Product

# Create your views here.


def product(request):
    q = Product.objects.all().values()
    print(q)

    return render(request, "prod.html", context={"product": q})


def addPage(request):

    return render(request, "addprod.html")


def productAdd(request):
    if request.method == "GET":
        data = request.GET

        p = Product(name=data["name"], desc=data["desc"],
                    price=data["price"], quantity=data["quantity"])
        p.save()
        print(data)

    if request.method == "POST":
        data = request.POST

        p = Product(name=data["name"], desc=data["desc"],
                    price=data["price"], quantity=data["quantity"])
        p.save()
        print(data)

    return HttpResponse("<h1> Data Added</h1>")
    return render(request, "added.html")
