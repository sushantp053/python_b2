from django.shortcuts import render
from django.http import HttpResponse
from product.models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


def register(request):
    if request.method == "POST":
        data = request.POST

        firstName = data["firstName"]
        lastName = data["lastName"]
        email = data["email"]
        password = data["password"]

        if (email != "" and password != ""):
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
                msg = "User has already registerd!"
                return render(request, "login.html")
        else:
            msg = "All credintials required."
            return render(request, "register.html")
    else:
        return render(request, "register.html")


def logOut(request):
    logout(request)

    return render(request, "login.html")


def addToCart(request):
    if request.method == "GET":
        prodId = request.GET["prodId"]

        p = Product.objects.get(id=prodId)
        print(p)

        Cart.objects.create(product_id=p, price=p.price,
                            quantity=1,  total=p.price,
                            user=request.user)

    q = Product.objects.all().values()

    return render(request, "prod.html", context={"product": q})


def login1(request):
    if request.method == "POST":
        data = request.POST
        email = data['email']
        password = data['password']

        # u = User.objects.filter(email=email, password=password).exists()
        user = authenticate(username=email, password=password)
        if (user != None):
            print(user)
            login(request, user)
            return HttpResponse("User Has been Successfully logged in")
        else:
            return HttpResponse("User Crenditials are wrong")

        print(user)
    return render(request, "login.html")


@login_required
def product(request):
    q = Product.objects.all().values()
    print(q)

    return render(request, "prod.html", context={"product": q})


@login_required
def address(request):
    if request.method == "POST":
        data = request.POST
        Address.objects.create(name=data["name"], building_name=data["building"],
                               flat=data["flat"], landmark=data["landmark"],
                               city=data["city"], pin=data["pin"], mobile=data["mobile"],
                               user=request.user)

    addr = Address.objects.filter(user=request.user)

    return render(request, "addr.html", context={"address": addr})


@login_required
def addrSelector(request):

    addr = Address.objects.filter(user=request.user)

    return render(request, "addr_selector.html", context={"address": addr})


@login_required
def confirmOrder(request):

    addrid = request.GET["addrid"]

    address = Address.objects.get(uid=addrid)

    cart = Cart.objects.filter(user=request.user)

    for c in cart:
        print(c)
        Order.objects.create(product_id=c.product_id, price=c.price,
                             quantity=c.quantity,  total=c.price,
                             user=request.user, addr=address)
        c.delete()

    return HttpResponse("Your orders has been confirmed")


@login_required
def cart(request):
    if request.method == "GET":
        try:
            prodId = request.GET["prodId"]
            d = Cart.objects.get(uid=prodId)
            d.delete()
        except:
            print("Error to fetch object")

    q = Cart.objects.filter(user=request.user)
    sum = 0
    count = 0
    for p in q:
        Product.objects.create
        p.delete
        sum = p.price + sum
        count = p.quantity + count

    return render(request, "cart.html", context={"product": q, "count": count, "sum": sum})


@login_required
def addPage(request):

    return render(request, "addprod.html")


@login_required
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
