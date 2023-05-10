from django.shortcuts import render
from django.http import JsonResponse
from pizza.models import HasP, Product, Topping, HasT

def main(request):
    pizzacontext = HasP.objects.all().select_related('PID').select_related('TID')
    toppingcontext = HasT.objects.select_related('TGID').select_related('TID')
    PizzaDict = sort_data(pizzacontext, toppingcontext, "1", False)
    return render(request, "menu.html", PizzaDict)

def filter(request):
    if request.method == 'GET':
        filter = request.GET['filter']
        sort = request.GET['sort']
        veg = False
        spicy = False
        
        if request.GET['veg'] == "true":
            veg = True
        if request.GET['spicy'] == "true":
            spicy = True

        pizzacontext = HasP.objects.filter().select_related('PID').select_related('TID')
        toppingcontext = HasT.objects.select_related('TGID').select_related('TID')
        PizzaDict = sort_data(pizzacontext, toppingcontext, sort, False)

        EditedPizzaDict = []
        for pizza in PizzaDict["pizzas"]:
            if pizza["name"].lower().find(filter.lower()) != -1:
                TagCondition = True
                if veg:
                    if not pizza["veg"]:
                        TagCondition = False
                if spicy:
                    if not pizza["spicy"]:
                        TagCondition = False
                if TagCondition:                      
                    EditedPizzaDict.append(pizza)
            
        return JsonResponse(EditedPizzaDict, safe=False)

def sort_data(context, toppingcontext, sort, view):
    lis = {}
    item_name = None

    toppinglis = {}
    for topping in toppingcontext:
        if topping.TID.name in toppinglis:
            toppinglis[topping.TID.name].append(topping.TGID.name)
        else:   
            toppinglis[topping.TID.name] = [topping.TGID.name]

    for object in context:
        if object.PID.name in lis:
            lis[object.PID.name]["toppings"] += ", " + object.TID.name
        else:
            lis[object.PID.name] = {"id": object.PID.id, "description": object.PID.description, "name": object.PID.name, "toppings": object.TID.name, "pricesmall": object.PID.pricesmall, "pricemedium": object.PID.pricemedium, "pricelarge": object.PID.pricelarge, "pic": object.PID.pic, "veg": True, "spicy": False}
            
            if view:
                item_name = object.PID.name

        if object.TID.name in toppinglis:
            if "Vegeterian" not in toppinglis[object.TID.name] :
                lis[object.PID.name]["veg"] = False
            if "Spicy" in toppinglis[object.TID.name]:
                lis[object.PID.name]["spicy"] = True
        else:
            lis[object.PID.name]["veg"] = False

    if view:
        value = lis.pop(item_name)
        return {"pizza": value}
    else:
        PizzaDict = {"pizzas": lis.values()}

    if sort == "1":
        PizzaDict["pizzas"] = sorted(PizzaDict["pizzas"], key=lambda x: x['name'])
    if sort == "2":
        PizzaDict["pizzas"] = sorted(PizzaDict["pizzas"], key=lambda x: x['name'], reverse=True)
    if sort == "3":
        PizzaDict["pizzas"] = sorted(PizzaDict["pizzas"], key=lambda x: x['pricelarge'])
    if sort == "4":
        PizzaDict["pizzas"] = sorted(PizzaDict["pizzas"], key=lambda x: x['pricelarge'], reverse=True)
 
 
    return PizzaDict

def pizzaview(request, pizza_id):
    context = Product.objects.filter(id=pizza_id)
    if not context:
        pizzacontext = HasP.objects.filter().select_related('PID').select_related('TID')
        toppingcontext = HasT.objects.select_related('TGID').select_related('TID')
        PizzaDict = sort_data(pizzacontext, toppingcontext, request.GET['sort'], False)
        return render(request, "menu.html", PizzaDict)
    else:
        pizzacontext = HasP.objects.all().select_related('PID').select_related('TID').filter(PID=pizza_id)
        toppingcontext = HasT.objects.select_related('TGID').select_related('TID')
        PizzaDict = sort_data(pizzacontext, toppingcontext, 0, True)
        PizzaDict["toppings"] = Topping.objects.all()
        return render(request, "pizzaview.html", PizzaDict)