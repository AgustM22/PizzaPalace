from django.shortcuts import render
from django.http import JsonResponse
from pizza.models import HasP 

def main(request):
    context = HasP.objects.all().select_related('PID').select_related('TID')
    PizzaDict = sort_data(context)

    return render(request, "menu.html", PizzaDict)

def filter(request):
    if request.method == 'GET':
        filter = request.GET['filter']
        context = HasP.objects.filter().select_related('PID').select_related('TID')
        PizzaDict = sort_data(context)
        EditedPizzaDict = []
        for pizza in PizzaDict["pizzas"]:
            if pizza["name"].lower().find(filter.lower()) != -1:
                EditedPizzaDict.append(pizza)
        return JsonResponse(EditedPizzaDict, safe=False)

def sort_data(context):
    lis = {}
    for object in context:
        if object.PID.name in lis:
            lis[object.PID.name]["toppings"] += ", " + object.TID.name
        else:
            lis[object.PID.name] = {"id": object.id, "name": object.PID.name, "toppings": object.TID.name, "pricesmall": object.PID.pricesmall, "pricemedium": object.PID.pricemedium, "pricelarge": object.PID.pricelarge, "pic": object.PID.pic}
    PizzaDict = {"pizzas": lis.values()}
    return PizzaDict