from django.shortcuts import render
from pizza.models import HasP 

def main(request):
    context = HasP.objects.all().select_related('PID').select_related('TID')
    lis = {}
    for object in context:
        if object.PID.name in lis:
            lis[object.PID.name]["toppings"] += ", " + object.TID.name
        else:
            lis[object.PID.name] = {"name": object.PID.name, "toppings": object.TID.name, "pricesmall": object.PID.pricesmall, "pricemedium": object.PID.pricemedium, "pricelarge": object.PID.pricelarge, "pic": object.PID.pic}
    newlis = {"pizzas": lis.values()}

    return render(request, "menu.html", newlis)