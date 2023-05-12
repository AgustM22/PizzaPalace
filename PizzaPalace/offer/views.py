from django.shortcuts import render
from django.http import JsonResponse
from pizza.models import Offer, Product

def main(request):
    """
    This view gets all the required information from offers and displays the offer menu.
    """
    context = Offer.objects.all()
    sort = "1"
    Offerlis = create_offer_list(context, sort)

    return render(request, "offer.html", {"offers": Offerlis})

def filter(request):
    """
    This filter is activated whenever the searchbar is typed into. It then returns the given data sorted by the string given.
    """
    if request.method == 'GET':
        filter = request.GET['filter']
        sort = request.GET['sort']
        context = Offer.objects.filter(name__icontains=filter)
        Offerlis = create_offer_list(context, sort)

        return JsonResponse(Offerlis, safe=False, status=200)

def create_offer_list(context, sort):
    """
    This function creates a list from a given querylist from the database.
    """
    Offerlis = []
    for object in context:
        templis = {"id": object.id, "name": object.name, "description": object.description, "price": object.price, "pic": object.pic}
        Offerlis.append(templis)
    
    if sort == "1": # Sorts the lists depending on sort.
        Offerlis = sorted(Offerlis, key=lambda x: x['name'])
    if sort == "2":
        Offerlis = sorted(Offerlis, key=lambda x: x['name'], reverse=True)
    if sort == "3":
        Offerlis = sorted(Offerlis, key=lambda x: x['price'])
    if sort == "4":
        Offerlis = sorted(Offerlis, key=lambda x: x['price'], reverse=True)

    return Offerlis

def offerview(request, offer_id):
    """
    This view is for viewing individual pizzas. It first checks whether the given id exists, before displaying it with all the necessary context.

    If it cannot find the given pizza id, it redirects to the menu.
    """
    context = Offer.objects.filter(id=offer_id)
    if not context:
        context = {'offers': Offer.objects.all()}
        return render(request, "offer.html", context)
    else:
        if offer_id == 1: # Two for One offer
            pizzacontext = Product.objects.all()
            return render(request, "offerview.html", {'offers': context, 'id':1, 'additionalContext': pizzacontext})
        if offer_id == 2: # Hottest Pizzas offer
            pizzacontext = Product.objects.get(id=1)
            return render(request, "offerview.html", {'offers': context, 'id':2, 'additionalContext': pizzacontext})