from django.shortcuts import render
from django.http import JsonResponse
from pizza.models import HasP, Product, Topping, HasT

def main(request):
    """
    Collects all the required information for the menu page before displaying it.
    """
    pizzacontext = HasP.objects.all().select_related('PID').select_related('TID')
    toppingcontext = HasT.objects.select_related('TGID').select_related('TID')
    PizzaDict = sort_data(pizzacontext, toppingcontext, "1", False)
    return render(request, "menu.html", PizzaDict)

def filter(request):
    """
    This view is refrenced whenever any new filters are added, such as tags or search any string in the menu.
    It takes in any new filters, sorts the total data from those filters, before sending it back to the same page.
    """
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
        for pizza in PizzaDict["pizzas"]: # checks if all pizzas have the requested filtered tags
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
            
        return JsonResponse(EditedPizzaDict, safe=False, status=200)

def sort_data(context, toppingcontext, sort, view):
    """
    Partial function of filter. Takes in main contexts before breaking down the given querylists by required values and sorts.
    """
    lis = {}
    item_name = None

    toppinglis = {}
    for topping in toppingcontext:
        if topping.TID.name in toppinglis: # First creates a list of tags from all toppings
            toppinglis[topping.TID.name].append(topping.TGID.name)
        else:   
            toppinglis[topping.TID.name] = [topping.TGID.name]

    for object in context: # Creates a list of pizzas, with all their toppings in one dictionary instead of multiple querylists
        if object.PID.name in lis:
            lis[object.PID.name]["toppings"] += ", " + object.TID.name
        else:
            lis[object.PID.name] = {"id": object.PID.id, "description": object.PID.description, "name": object.PID.name, "toppings": object.TID.name, "pricesmall": object.PID.pricesmall, "pricemedium": object.PID.pricemedium, "pricelarge": object.PID.pricelarge, "pic": object.PID.pic, "veg": True, "spicy": False}
            
            if view:
                item_name = object.PID.name

        if object.TID.name in toppinglis: # Gives each pizza appropriate tags 
            if "Vegeterian" not in toppinglis[object.TID.name] :
                lis[object.PID.name]["veg"] = False
            if "Spicy" in toppinglis[object.TID.name]:
                lis[object.PID.name]["spicy"] = True
        else:
            lis[object.PID.name]["veg"] = False

    if view: # If you're viewing a pizza, you only need one.
        value = lis.pop(item_name)
        return {"pizza": value}
    else:
        PizzaDict = {"pizzas": lis.values()}

    if sort == "1": # Sorts the dictionary of pizzas depending on the sort given.
        PizzaDict["pizzas"] = sorted(PizzaDict["pizzas"], key=lambda x: x['name'])
    if sort == "2":
        PizzaDict["pizzas"] = sorted(PizzaDict["pizzas"], key=lambda x: x['name'], reverse=True)
    if sort == "3":
        PizzaDict["pizzas"] = sorted(PizzaDict["pizzas"], key=lambda x: x['pricelarge'])
    if sort == "4":
        PizzaDict["pizzas"] = sorted(PizzaDict["pizzas"], key=lambda x: x['pricelarge'], reverse=True)
 
    return PizzaDict

def pizzaview(request, pizza_id):
    """
    This view is for viewing individual pizzas. It first checks whether the given id exists, before displaying it with all the necessary context.

    If it cannot find the given pizza id, it redirects to the menu.
    """    
    context = Product.objects.filter(id=pizza_id)
    if not context: # If the pizza
        pizzacontext = HasP.objects.filter().select_related('PID').select_related('TID')
        toppingcontext = HasT.objects.select_related('TGID').select_related('TID')
        PizzaDict = sort_data(pizzacontext, toppingcontext, request.GET['sort'], False)
        return render(request, "menu.html", PizzaDict)
    else:
        pizzacontext = HasP.objects.all().select_related('PID').select_related('TID').filter(PID=pizza_id)
        toppingcontext = HasT.objects.select_related('TGID').select_related('TID')
        PizzaDict = sort_data(pizzacontext, toppingcontext, 0, True)
        PizzaDict["toppings"] = Topping.objects.all().select_related('FID')
        return render(request, "pizzaview.html", PizzaDict)