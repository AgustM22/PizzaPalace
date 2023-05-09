from django.shortcuts import render
from django.http import JsonResponse


cartdata = [
    {
        "name": "Margharita",
        "ingredients": "Cheese, Sauce",
        "picture": "https://media.istockphoto.com/id/1280329631/photo/italian-pizza-margherita-with-tomatoes-and-mozzarella-cheese-on-wooden-cutting-board-close-up.jpg?b=1&s=170667a&w=0&k=20&c=_t83ocY59IayPnspluN99xOM_RQ5ytAMTfXQperbL_I=",
        "tags": [
            "vegetarian"
        ],
        "price": "1.000.kr",
        "quantity": "1"
    },
        {
        "name": "Margharita",
        "ingredients": "Cheese, Sauce",
        "picture": "https://media.istockphoto.com/id/1280329631/photo/italian-pizza-margherita-with-tomatoes-and-mozzarella-cheese-on-wooden-cutting-board-close-up.jpg?b=1&s=170667a&w=0&k=20&c=_t83ocY59IayPnspluN99xOM_RQ5ytAMTfXQperbL_I=",
        "tags": [
            "vegetarian"
        ],
        "price": "1.000.kr",
        "quantity": "1"
    },
        {
        "name": "Margharita",
        "ingredients": "Cheese, Sauce",
        "picture": "https://media.istockphoto.com/id/1280329631/photo/italian-pizza-margherita-with-tomatoes-and-mozzarella-cheese-on-wooden-cutting-board-close-up.jpg?b=1&s=170667a&w=0&k=20&c=_t83ocY59IayPnspluN99xOM_RQ5ytAMTfXQperbL_I=",
        "tags": [
            "vegetarian"
        ],
        "price": "1.000.kr",
        "quantity": "1"
    },
            {
        "name": "Margharita",
        "ingredients": "Cheese, Sauce",
        "picture": "https://media.istockphoto.com/id/1280329631/photo/italian-pizza-margherita-with-tomatoes-and-mozzarella-cheese-on-wooden-cutting-board-close-up.jpg?b=1&s=170667a&w=0&k=20&c=_t83ocY59IayPnspluN99xOM_RQ5ytAMTfXQperbL_I=",
        "tags": [
            "vegetarian"
        ],
        "price": "1.000.kr",
        "quantity": "1"
    },
                {
        "name": "Margharita",
        "ingredients": "Cheese, Sauce",
        "picture": "https://media.istockphoto.com/id/1280329631/photo/italian-pizza-margherita-with-tomatoes-and-mozzarella-cheese-on-wooden-cutting-board-close-up.jpg?b=1&s=170667a&w=0&k=20&c=_t83ocY59IayPnspluN99xOM_RQ5ytAMTfXQperbL_I=",
        "tags": [
            "vegetarian"
        ],
        "price": "1.000.kr",
        "quantity": "1"
    },
                {
        "name": "Margharita",
        "ingredients": "Cheese, Sauce",
        "picture": "https://media.istockphoto.com/id/1280329631/photo/italian-pizza-margherita-with-tomatoes-and-mozzarella-cheese-on-wooden-cutting-board-close-up.jpg?b=1&s=170667a&w=0&k=20&c=_t83ocY59IayPnspluN99xOM_RQ5ytAMTfXQperbL_I=",
        "tags": [
            "vegetarian"
        ],
        "price": "1.000.kr",
        "quantity": "1"
    },
                {
        "name": "Margharita",
        "ingredients": "Cheese, Sauce",
        "picture": "https://media.istockphoto.com/id/1280329631/photo/italian-pizza-margherita-with-tomatoes-and-mozzarella-cheese-on-wooden-cutting-board-close-up.jpg?b=1&s=170667a&w=0&k=20&c=_t83ocY59IayPnspluN99xOM_RQ5ytAMTfXQperbL_I=",
        "tags": [
            "vegetarian"
        ],
        "price": "1.000.kr",
        "quantity": "1"
    },
    
    
]

def main(request):
    if not request.session.get('cart'):
        createcart(request)

    return render(request, "CreditCardDetails.html", context = request.session['cart'])

def createcart(request):
    request.session['cart'] = {"pizzas": [], "offers": [], "fullprice": 0}

def addToCart(request):
    if not request.session.get('cart'):
        createcart(request)

    newpizza = {"name": str(request.GET['name']), "price": str(request.GET['price']), "qty": int(request.GET['qty']), "additionaltoppings": str(request.GET['additionaltoppings'])}
    if request.GET['type'] == "pizza":
        if request.session['cart']["pizzas"] == []:
            request.session['cart']["pizzas"] = [newpizza]
            request.session['cart']['fullprice'] += int(newpizza['price'][0:-3])
        else:
            found = False
            for item in request.session['cart']["pizzas"]:
                if item["name"] == newpizza["name"] and item["price"] == newpizza["price"] and item["additionaltoppings"] == newpizza["additionaltoppings"]:
                    item["qty"] += 1
                    found  = True
                    request.session['cart']['fullprice'] += int(newpizza['price'][0:-3])
            if not found:
                request.session['cart']["pizzas"].append(newpizza)
                request.session['cart']['fullprice'] += int(newpizza['price'][0:-3])
    else:
        pass
    
    request.session.modified = True
    return JsonResponse(100, safe=False)

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
    return JsonResponse(100, safe=False)