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
        "name": "Hawaiian",
        "ingredients": "Cheese, Sauce, pineapple",
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
    const pizzaText = document.createElement("div")
    const pizzaPrices = document.createElement("div")
    pizzaElement.setAttribute("class", "PizzaElement")
    pizzaText.setAttribute("class", "PizzaText")
    pizzaPrices.setAttribute("class", "PizzaPrices")
    
    const pizzaName = document.createElement("h1")
    const pizzaIngredients = document.createElement("p")
    const pizzaImg = document.createElement("img")

    const priceSmall = document.createElement("p")
    const priceMedium = document.createElement("p")
    const PriceLarge = document.createElement("p")
    priceSmall.innerText = "Small: " + pizza.price.small
    priceMedium.innerText = "Medium: " + pizza.price.medium
    PriceLarge.innerText = "Large: " + pizza.price.large
    
    pizzaName.innerText = pizza.name
    pizzaName.setAttribute("class", "PizzaName")
    pizzaIngredients.innerText = pizza.ingredients
    pizzaIngredients.setAttribute("class", "PizzaIngredients")

    pizzaImg.setAttribute("src", pizza.picture)
    pizzaImg.setAttribute("class", "PizzaImg")
    pizzaImg.setAttribute("alt", "PizzaImg")

    pizzaElement.appendChild(pizzaImg)

    pizzaText.appendChild(pizzaName)
    pizzaText.appendChild(pizzaIngredients)
    pizzaElement.appendChild(pizzaText)

    pizzaPrices.appendChild(priceSmall)
    pizzaPrices.appendChild(priceMedium)
    pizzaPrices.appendChild(PriceLarge)
    pizzaElement.appendChild(pizzaPrices)

    PizzaBox.appendChild(pizzaElement)
}
