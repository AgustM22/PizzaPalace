from django.shortcuts import render , redirect
from django.http import JsonResponse, HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from user.forms.ProfileForm import ProfileForm,CreditCardForm
from user.models import UserProfile, CreditCard

def main(request):
    """
    The main view for rendering the cart.
    """
    if not request.session.get('cart'):
        createcart(request)

    return render(request, "CartView.html", context = request.session['cart'])

@login_required
def contactinformation(request):
    """
    This view renders all the necessary information for the contact information step of purchasing.
    If there occurs an error from "checkcontactinformation", it is re-rendered with an error message.
    """
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
        
    if request.session['cart'] == {"pizzas": [], "offers": [], "fullprice": 0,"isprepaid":False}: 
        return render(request, "Homepage.html")
    
    check = request.GET.get('e' , '')
    if check != '': # On error...
        return render(request, "ContactInformation.html", context={'form':ProfileForm(instance=profile),'pizzas':pizzas,'offers':offers,'fullprice':fullprice, "error": True,"isprepaid":False})

    return render(request, "ContactInformation.html", context={'form':ProfileForm(instance=profile),'pizzas':pizzas,'offers':offers,'fullprice':fullprice,"isprepaid":False})

def checkcontactinformation(request):
    """
    This view checks if all the forms of "contactinformation" are filled. If so, redirects to checkout, if not, then it re-renders contactinformation with an error message.
    """
    profile = UserProfile.objects.filter(user=request.user).first()
    if request.method == 'POST':
        form = ProfileForm(instance=profile,data=request.POST)
        if form.is_valid():
            return HttpResponseRedirect('/cart/creditcard')
        else:
            return HttpResponseRedirect('/cart/checkout?e=1')

def createcart(request):
    """
    Creates a cookie cart.
    """
    request.session['cart'] = {"pizzas": [], "offers": [], "fullprice": 0,"isprepaid":False}

def addToCart(request):
    """
    Adds a product to the cart and maintains the correct information, such as full price.
    """
    if not request.session.get('cart'):
        createcart(request)

    if request.GET['type'] == "pizza": # Adding pizza to cart
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
    else: # Adding offer to cart
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
    """
    Returns all information in cart.
    """
    if not request.session.get('cart'):
        createcart(request)

    return JsonResponse(request.session['cart'], safe=False)
    
def editcart(request):
    """
    This function edits the values of the product sent through. Maintains fullprice and qty and saves it to the cart. 
    """
    wipecheck = request.GET.get('wipe', False)
    print(wipecheck)

    if wipecheck == "true":
        print("I AM IN")
        request.session['cart'] = {"pizzas": [], "offers": [], "fullprice": 0}
        request.session.modified = True
        return HttpResponse("", status=200)

    newproduct = {"name": str(request.GET['name']), "price": str(request.GET['price']), "qty": int(request.GET['qty']), "extra": str(request.GET['extra'])}
    if request.GET['remove'] == "true": # If a product needs to be removed.
        for item in request.session['cart']["pizzas"]:
            if item["name"] == newproduct["name"] and item["price"] == newproduct["price"] and item["additionaltoppings"] == newproduct["extra"]:
                request.session['cart']["pizzas"].remove(item)
        for item in request.session['cart']["offers"]:
            if item["name"] == newproduct["name"] and item["price"] == newproduct["price"] and item["item"] == newproduct["extra"]:
                request.session['cart']["offers"].remove(item)
        
        FullPrice = 0 # Calculates full price on removal
        for item in request.session['cart']["pizzas"]:
            FullPrice += int(item["price"]) * int(item["qty"])
        for item in request.session['cart']["offers"]:
            FullPrice += int(item["price"]) * int(item["qty"])
        request.session['cart']["fullprice"] = FullPrice

        request.session.modified = True
        return HttpResponse("", status=200)
    
    for item in request.session['cart']["offers"]: # If the quantity of a product has been changed.
        if item["name"] == newproduct["name"] and item["price"] == newproduct["price"] and item["item"] == newproduct["extra"]:
            request.session['cart']['fullprice'] += (int(newproduct["qty"]) - int(item["qty"])) * int(newproduct["price"]) # Edits fullprice on quantity change
            item["qty"] = newproduct["qty"]
    for item in request.session['cart']["pizzas"]:
        if item["name"] == newproduct["name"] and item["price"] == newproduct["price"] and item["additionaltoppings"] == newproduct["extra"]:
            request.session['cart']['fullprice'] += (int(newproduct["qty"]) - int(item["qty"])) * int(newproduct["price"])
            item["qty"] = newproduct["qty"]

    request.session.modified = True
    return HttpResponse("")

def checkcreditcard(request):
    """
    This view checks if all the forms of "creditcard" are filled. If so, redirects to the overview step, if not, then it re-renders creditcard with an error message.
    """
    profile = CreditCard.objects.filter(user=request.user).first()
    if request.method == 'POST':
        form = CreditCardForm(instance=profile,data=request.POST)
        if form.is_valid():
            return HttpResponseRedirect('/cart/overview')
        else:
            return HttpResponseRedirect('/cart/creditcard?e=1')

@login_required
def creditcard(request):
    """
    This view renders all the necessary information for the credit card information step of purchasing.
    If there occurs an error from "checkcreditcard", it is re-rendered with an error message.
    """
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
            cart["isprepaid"] = True
            request.session.modified = True
            return redirect('overview')
        
    if request.session['cart'] == {"pizzas": [], "offers": [], "fullprice": 0,"isprepaid":False}: # If the user ever calls the page through URL manually, then this check should redirect them to the homepage. 
        return render(request, "Homepage.html")
    
    check = request.GET.get('e' , '')
    if check != '': # On error... (Is only ever called if the checkcreditcart notices an empty field)
        return render(request, "CreditCardDetails.html", context={'form':CreditCardForm(instance=profile),'pizzas':pizzas,'offers':offers,'fullprice':fullprice, "error": True,"isprepaid":False})
    
    return render(request, "CreditCardDetails.html", context={'form':CreditCardForm(instance=profile),'pizzas':pizzas,'offers':offers,'fullprice':fullprice,"isprepaid":False})

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
    isprepaid = cart["isprepaid"]
    if request.session['cart'] == {"pizzas": [], "offers": [], "fullprice": 0,"isprepaid":False}: #If cart is empty
        return render(request, "Homepage.html")
    return render(request, "overview.html", context={'profileform': ProfileForm(instance=profile), 'creditcardform': CreditCardForm(instance=creditcard), 'pizzas':pizzas,'offers':offers,'fullprice':fullprice,"isprepaid":isprepaid})

def deletecart(request):
    """
    Wipes the cart and redirects to the confirmation page
    """
    del request.session['cart']
    request.session.modified = True
    return HttpResponseRedirect('/confirmation')