seed = [
    {
        "name": "Margharita",
        "ingredients": "Cheese, Sauce",
        "picture": "https://media.istockphoto.com/id/1280329631/photo/italian-pizza-margherita-with-tomatoes-and-mozzarella-cheese-on-wooden-cutting-board-close-up.jpg?b=1&s=170667a&w=0&k=20&c=_t83ocY59IayPnspluN99xOM_RQ5ytAMTfXQperbL_I=",
        "tags": [
            "vegetarian"
        ],
        "price": {
            "small": "1.800kr",
            "medium": "1.800kr",
            "large": "1.800kr"
        }
    },
    {
        "name": "Margharita",
        "ingredients": "Cheese, Sauce",
        "picture": "https://media.istockphoto.com/id/1280329631/photo/italian-pizza-margherita-with-tomatoes-and-mozzarella-cheese-on-wooden-cutting-board-close-up.jpg?b=1&s=170667a&w=0&k=20&c=_t83ocY59IayPnspluN99xOM_RQ5ytAMTfXQperbL_I=",
        "tags": [
            "vegetarian"
        ],
        "price": {
            "small": "1.800kr",
            "medium": "1.800kr",
            "large": "1.800kr"
        }
    },
    {
        "name": "Margharita",
        "ingredients": "Cheese, Sauce",
        "picture": "https://media.istockphoto.com/id/1280329631/photo/italian-pizza-margherita-with-tomatoes-and-mozzarella-cheese-on-wooden-cutting-board-close-up.jpg?b=1&s=170667a&w=0&k=20&c=_t83ocY59IayPnspluN99xOM_RQ5ytAMTfXQperbL_I=",
        "tags": [
            "vegetarian"
        ],
        "price": {
            "small": "1.800kr",
            "medium": "1.800kr",
            "large": "1.800kr"
        }
    },
    {
        "name": "Margharita",
        "ingredients": "Cheese, Sauce",
        "picture": "https://media.istockphoto.com/id/1280329631/photo/italian-pizza-margherita-with-tomatoes-and-mozzarella-cheese-on-wooden-cutting-board-close-up.jpg?b=1&s=170667a&w=0&k=20&c=_t83ocY59IayPnspluN99xOM_RQ5ytAMTfXQperbL_I=",
        "tags": [
            "vegetarian"
        ],
        "price": {
            "small": "1.800kr",
            "medium": "1.800kr",
            "large": "1.800kr"
        }
    },
    {
        "name": "Clayo",
        "ingredients": "Clay, Mayo",
        "picture": "https://media.istockphoto.com/id/1280329631/photo/italian-pizza-margherita-with-tomatoes-and-mozzarella-cheese-on-wooden-cutting-board-close-up.jpg?b=1&s=170667a&w=0&k=20&c=_t83ocY59IayPnspluN99xOM_RQ5ytAMTfXQperbL_I=",
        "tags": [
            "vegetarian"
        ],
        "price": {
            "small": "1.800kr",
            "medium": "1.800kr",
            "large": "1.800kr"
        }
    }
]


const SearchFilter = () => {
    const Main = document.getElementById("PizzaBox")
    Main.innerHTML = ""

	const SearchText = document.getElementById("search").value
    const pizzas = [...seed];
    const PizzaArray = []
	
	pizzas.forEach((pizza) => {
		if (pizza.name.toLowerCase().includes(SearchText.toLowerCase())) {
			PizzaArray.push(pizza)
		}
	})

    PizzaArray.forEach((pizza) => {
        PopulatePizzaBox(pizza)
    })
}

const PopulatePizzaBox = (pizza) => {
    const PizzaBox = document.getElementById("PizzaBox")

    const pizzaElement = document.createElement("div")
    pizzaElement.setAttribute("class", "PizzaElement")
    
    const pizzaName = document.createElement("h1")
    const pizzaIngredients = document.createElement("p")
    const pizzaImg = document.createElement("img")
    pizzaName.innerText = pizza.name
    pizzaName.setAttribute("class", "PizzaName")
    pizzaIngredients.innerText = pizza.ingredients
    pizzaIngredients.setAttribute("class", "PizzaIngredients")
    pizzaImg.setAttribute("src", pizza.picture)
    pizzaImg.setAttribute("class", "PizzaImg")
    pizzaImg.setAttribute("alt", "PizzaImg")

    pizzaElement.appendChild(pizzaImg)
    pizzaElement.appendChild(pizzaName)
    pizzaElement.appendChild(pizzaIngredients)
    PizzaBox.appendChild(pizzaElement)
}
