from django.shortcuts import render
from django.http import JsonResponse
from pizza.models import Offer, Product

def main(request):
    context = Offer.objects.all()
    sort = "1"
    Offerlis = create_offer_list(context, sort)

    return render(request, "offer.html", {"offers": Offerlis})

def filter(request):
    if request.method == 'GET':
        filter = request.GET['filter']
        sort = request.GET['sort']
        context = Offer.objects.filter(name__icontains=filter)
        Offerlis = create_offer_list(context, sort)

        return JsonResponse(Offerlis, safe=False)

def create_offer_list(context, sort):
    Offerlis = []
    for object in context:
        templis = {"id": object.id, "name": object.name, "description": object.description, "price": object.price, "pic": object.pic}
        Offerlis.append(templis)
    
    if sort == "1":
        Offerlis = sorted(Offerlis, key=lambda x: x['name'])
    if sort == "2":
        Offerlis = sorted(Offerlis, key=lambda x: x['name'], reverse=True)
    if sort == "3":
        Offerlis = sorted(Offerlis, key=lambda x: x['price'])
    if sort == "4":
        Offerlis = sorted(Offerlis, key=lambda x: x['price'], reverse=True)

    return Offerlis

def offerview(request, offer_id):
    context = Offer.objects.filter(id=offer_id)
    if not context:
        context = {'offers': Offer.objects.all()}
        return render(request, "offer.html", context)
    else:
        if offer_id == 1:
            pizzacontext = Product.objects.all()
            return render(request, "offerview.html", {'offers': context, 'id':1, 'additionalContext': pizzacontext})
        if offer_id == 2:
            pizzacontext = Product.objects.get(id=1)
            return render(request, "offerview.html", {'offers': context, 'id':2, 'additionalContext': pizzacontext})