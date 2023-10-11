from django.shortcuts import render
from django.http import HttpResponse
from product.models import Product
from django.contrib.auth.models import User


def register(request):
    if request.method == "POST":
        print("Post method called")
        data = request.POST

        firstName = data["firstName"]
        lastName = data["lastName"]
        email = data["email"]
        password = data["password"]

        if (email != "" and password != ""):
            print("email validated")
            if (not User.objects.filter(username=email).exists()):
                print("Email not existed")

                u = User.objects.create(first_name=firstName,
                                        last_name=lastName,
                                        username=email,
                                        email=email)
                u.set_password(password)
                u.save()
                msg = "User has been registerd please login now"
                return render(request, "login.html")
            else:
                print("email exitsted")
                msg = "User has already registerd!"
                return render(request, "login.html")
        else:
            print("Credintial not found")
            msg = "All credintials required."
            return render(request, "register.html")
    else:
        return render(request, "register.html")


def product(request):
    q = Product.objects.all().values()
    print(q)

    return render(request, "prod.html", context={"product": q})


def addPage(request):

    return render(request, "addprod.html")


def delete(request):
    if request.method == "GET":
        data = request.GET
        pid = data["prodId"]
        p = Product.objects.get(id=pid)
        p.delete()

    q = Product.objects.all().values()
    return render(request, "prod.html", context={"product": q})


def productAdd(request):
    if request.method == "GET":
        print("Get method called")
        data = request.GET

        p = Product(name=data["name"], desc=data["desc"],
                    price=data["price"], quantity=data["quantity"])
        p.save()
        print(data)

    if request.method == "POST":
        print("Post method called")
        data = request.POST

        p = Product(name=data["name"], desc=data["desc"],
                    price=data["price"], quantity=data["quantity"])
        p.save()
        print(data)

    return HttpResponse("<h1> Data Added</h1>")
    return render(request, "added.html")
