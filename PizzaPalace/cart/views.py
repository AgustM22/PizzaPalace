from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.contrib.auth.decorators import login_required
from user.forms.ProfileForm import ProfileForm
from user.models import UserProfile

def main(request):
    if not request.session.get('cart'):
        createcart(request)

    return render(request, "CartView.html", context = request.session['cart'])

@login_required
def checkout(request):
    profile = UserProfile.objects.filter(user=request.user).first()
    cart = request.session['cart']
    pizzas = cart['pizzas']
    offers = cart['offers']
    fullprice = cart['fullprice']
    if not request.session.get('cart'):
        return render(request, "Homepage.html")
    if request.method == 'POST':
        form = ProfileForm(instance=profile,data=request.POST)
        if form.is_valid():
            print("Made it here")
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
    return render(request, "CreditCardDetails.html",context={'form':ProfileForm(instance=profile),'pizzas':pizzas,'offers':offers,'fullprice':fullprice})

def createcart(request):
    request.session['cart'] = {"pizzas": [], "offers": [], "fullprice": 0}

def addToCart(request):
    if not request.session.get('cart'):
        createcart(request)

    if request.GET['type'] == "pizza":
        newpizza = {"name": str(request.GET['name']), "price": str(request.GET['price']), "qty": int(request.GET['qty']), "additionaltoppings": str(request.GET['additionaltoppings']), "img": str(request.GET['img'])}
        found = False
        for item in request.session['cart']["pizzas"]:
            if item["name"] == newpizza["name"] and item["price"] == newpizza["price"] and item["additionaltoppings"] == newpizza["additionaltoppings"]:
                item["qty"] += 1
                found  = True
                request.session['cart']['fullprice'] += int(newpizza['price'])
        if not found:
            request.session['cart']["pizzas"].append(newpizza)
            request.session['cart']['fullprice'] += int(newpizza['price'])
    else:
        newoffer = {"name": str(request.GET['name']), "price": str(request.GET['price']), "qty": int(request.GET['qty']), "item": (request.GET['item']), "img": str(request.GET['img'])}
        found = False
        for item in request.session['cart']["offers"]:
            if item["name"] == newoffer["name"] and item["price"] == newoffer["price"] and item["item"] == newoffer["item"]:
                item["qty"] += 1
                found  = True
                request.session['cart']['fullprice'] += int(newoffer['price'])
        if not found:
            request.session['cart']["offers"].append(newoffer)
            request.session['cart']['fullprice'] += int(newoffer['price'])

    request.session.modified = True
    return HttpResponse("")

def getcart(request):
    if not request.session.get('cart'):
        createcart(request)

    return JsonResponse(request.session['cart'], safe=False)

def deletecart(request):
    try:
        del request.session['cart']
    except KeyError:
        pass

    request.session.modified = True
    return HttpResponse("")

def editcart(request):
    newproduct = {"name": str(request.GET['name']), "price": str(request.GET['price']), "qty": int(request.GET['qty']), "extra": str(request.GET['extra'])}
    for item in request.session['cart']["offers"]:
        if item["name"] == newproduct["name"] and item["price"] == newproduct["price"] and item["item"] == newproduct["extra"]:
            request.session['cart']['fullprice'] += (int(newproduct["qty"]) - int(item["qty"])) * int(newproduct["price"])
            item["qty"] = newproduct["qty"]
    for item in request.session['cart']["pizzas"]:
        if item["name"] == newproduct["name"] and item["price"] == newproduct["price"] and item["additionaltoppings"] == newproduct["extra"]:
            request.session['cart']['fullprice'] += (int(newproduct["qty"]) - int(item["qty"])) * int(newproduct["price"])
            item["qty"] = newproduct["qty"]

    request.session.modified = True
    return HttpResponse("")