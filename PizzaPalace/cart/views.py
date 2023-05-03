from django.shortcuts import render

cart = [
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
    return render(request, "CartView.html",context= {"cart":cart})
