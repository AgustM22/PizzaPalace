from django.shortcuts import render
from django.http import JsonResponse
from pizza.models import HasP, Product, Topping

def main(request):
    context = HasP.objects.all().select_related('PID').select_related('TID')
    PizzaDict = sort_data(context, False)

    return render(request, "menu.html", PizzaDict)

def filter(request):
    if request.method == 'GET':
        filter = request.GET['filter']
        context = HasP.objects.filter().select_related('PID').select_related('TID')
        PizzaDict = sort_data(context, False)
        EditedPizzaDict = []
        for pizza in PizzaDict["pizzas"]:
            if pizza["name"].lower().find(filter.lower()) != -1:
                EditedPizzaDict.append(pizza)
        return JsonResponse(EditedPizzaDict, safe=False)

def sort_data(context, view):
    lis = {}
    item_name = None
    for object in context:
        if object.PID.name in lis:
            lis[object.PID.name]["toppings"] += ", " + object.TID.name
        else:
            lis[object.PID.name] = {"id": object.PID.id, "description": object.PID.description, "name": object.PID.name, "toppings": object.TID.name, "pricesmall": object.PID.pricesmall, "pricemedium": object.PID.pricemedium, "pricelarge": object.PID.pricelarge, "pic": object.PID.pic}
            if view:
                item_name = object.PID.name
    if view:
        value = lis.pop(item_name)
        return {"pizza": value}
    else:
        PizzaDict = {"pizzas": lis.values()}
        return PizzaDict

def pizzaview(request, pizza_id):
    context = Product.objects.filter(id=pizza_id)
    if not context:
        context = HasP.objects.all().select_related('PID').select_related('TID')
        PizzaDict = sort_data(context, False)
        return render(request, "menu.html", PizzaDict)
    else:
        context = HasP.objects.all().select_related('PID').select_related('TID').filter(PID=pizza_id)
        PizzaDict = sort_data(context, True)
        PizzaDict["toppings"] = Topping.objects.all()
        return render(request, "pizzaview.html", PizzaDict)