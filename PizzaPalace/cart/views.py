from django.shortcuts import render , redirect
from django.http import JsonResponse, HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from user.forms.ProfileForm import ProfileForm,CreditCardForm
from user.models import UserProfile, CreditCard

def main(request):
    if not request.session.get('cart'):
        createcart(request)

    return render(request, "CartView.html", context = request.session['cart'])

@login_required
def contactinformation(request):
    """View for contact information during the checkout phase"""
    profile = UserProfile.objects.filter(user=request.user).first()

    #We need all the information about what products are in the cart
    if not request.session.get('cart'):
        createcart(request)
    cart = request.session['cart']
    pizzas = cart['pizzas']
    offers = cart['offers']
    fullprice = cart['fullprice']

    if request.method == 'POST':
        form = ProfileForm(instance=profile,data=request.POST)
        temp = profile.ProfilePic
        if form.is_valid():
            profile = form.save(commit=False)
            profile.ProfilePic = temp
            profile.user = request.user
            profile.save()
            return redirect('creditcard')
        
    if request.session['cart'] == {"pizzas": [], "offers": [], "fullprice": 0}: #If the cart is empty return to homepage?
        return render(request, "Homepage.html")
    
    check = request.GET.get('e' , '') #Eh what? error check? dono if it ever makes it here...
    if check != '':
        return render(request, "ContactInformation.html", context={'form':ProfileForm(instance=profile),'pizzas':pizzas,'offers':offers,'fullprice':fullprice, "error": True})

    return render(request, "ContactInformation.html", context={'form':ProfileForm(instance=profile),'pizzas':pizzas,'offers':offers,'fullprice':fullprice})

def checkcontactinformation(request):
    profile = UserProfile.objects.filter(user=request.user).first()
    if request.method == 'POST':
        form = ProfileForm(instance=profile,data=request.POST)
        if form.is_valid():
            return HttpResponseRedirect('/cart/creditcard')
        else:
            return HttpResponseRedirect('/cart/checkout?e=1')

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
    
def editcart(request):
    wipecheck = request.GET.get('wipe', False)
    if wipecheck == "true":
        request.session['cart'] = {"pizzas": [], "offers": [], "fullprice": 0}
        request.session.modified = True
        return HttpResponse("")

    newproduct = {"name": str(request.GET['name']), "price": str(request.GET['price']), "qty": int(request.GET['qty']), "extra": str(request.GET['extra'])}
    if request.GET['remove'] == "true":
        for item in request.session['cart']["pizzas"]:
            if item["name"] == newproduct["name"] and item["price"] == newproduct["price"] and item["additionaltoppings"] == newproduct["extra"]:
                request.session['cart']["pizzas"].remove(item)
        for item in request.session['cart']["offers"]:
            if item["name"] == newproduct["name"] and item["price"] == newproduct["price"] and item["item"] == newproduct["extra"]:
                request.session['cart']["offers"].remove(item)
        
        FullPrice = 0
        for item in request.session['cart']["pizzas"]:
            FullPrice += int(item["price"]) * int(item["qty"])
        for item in request.session['cart']["offers"]:
            FullPrice += int(item["price"]) * int(item["qty"])
        request.session['cart']["fullprice"] = FullPrice

        request.session.modified = True
        return HttpResponse("")
    
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

def checkcreditcard(request):
    profile = CreditCard.objects.filter(user=request.user).first()
    if request.method == 'POST':
        form = CreditCardForm(instance=profile,data=request.POST)
        if form.is_valid():
            return HttpResponseRedirect('/cart/overview')
        else:
            return HttpResponseRedirect('/cart/creditcard?e=1')

@login_required
def creditcard(request):
    """View for entering in the credit card information"""
    profile = CreditCard.objects.filter(user=request.user).first()
    
    #We need to get the cart from the session
    if not request.session.get('cart'):
        createcart(request)
    cart = request.session['cart']
    pizzas = cart['pizzas']
    offers = cart['offers']
    fullprice = cart['fullprice']

    if request.method == 'POST':
        form = CreditCardForm(instance=profile,data=request.POST)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            return redirect('overview')
        
    if request.session['cart'] == {"pizzas": [], "offers": [], "fullprice": 0}: #If the cart is empty?
        return render(request, "Homepage.html")
    
    check = request.GET.get('e' , '') #Dno here ?
    if check != '':
        return render(request, "CreditCardDetails.html", context={'form':CreditCardForm(instance=profile),'pizzas':pizzas,'offers':offers,'fullprice':fullprice, "error": True})
    
    return render(request, "CreditCardDetails.html", context={'form':CreditCardForm(instance=profile),'pizzas':pizzas,'offers':offers,'fullprice':fullprice})

@login_required
def overview(request):
    """
    This view is read only. here we only want to display all the information for the user such as what is in their cart and all of their information.
    then when the user sends a post request we wipe the cart.
    """

    profile = UserProfile.objects.filter(user=request.user).first()
    creditcard = CreditCard.objects.filter(user=request.user).first()
    if not request.session.get('cart'):
        createcart(request)

    cart = request.session['cart']
    pizzas = cart['pizzas']
    offers = cart['offers']
    fullprice = cart['fullprice']

    if request.session['cart'] == {"pizzas": [], "offers": [], "fullprice": 0}:
        return render(request, "Homepage.html")
    return render(request, "overview.html", context={'profileform': ProfileForm(instance=profile), 'creditcardform': CreditCardForm(instance=creditcard), 'pizzas':pizzas,'offers':offers,'fullprice':fullprice})

def deletecart(request):
    """Wipes the cart and redirects to the confirmation page"""
    del request.session['cart']
    request.session.modified = True
    return HttpResponseRedirect('/confirmation')
