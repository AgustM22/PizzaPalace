const seed = [
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
        "ingredients": "Clay and Mayo",
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
] // Will have to change this to database

const Menu = () => {
    const Main = document.getElementById("MainBlock")
    Main.innerHTML = ""

    const SearchBar = document.createElement("div")
    const PizzaBox = document.createElement("div")
    const Search = document.createElement("input")
    const PizzaText = document.createElement("p")
    const Sliders = document.createElement("img")

    SearchBar.setAttribute("id", "SearchBar")
    PizzaBox.setAttribute("id", "PizzaBox")

    Search.setAttribute("placeholder", "Search...")
    Search.setAttribute("oninput", "SearchFilter()")
    Search.setAttribute("id", "search")
    PizzaText.innerText = "Pizza"
    Sliders.setAttribute("id", "SliderSettings")
    Sliders.setAttribute("alt", "Settings")
    Sliders.setAttribute("src", "/static/images/sliders.svg")

    SearchBar.appendChild(Search)
    SearchBar.appendChild(PizzaText)
    SearchBar.appendChild(Sliders)
    Main.appendChild(SearchBar)
    Main.appendChild(PizzaBox)

    const pizzas = [...seed];

    pizzas.forEach((pizza) => {
        PopulatePizzaBox(pizza)
    })
}

const SearchFilter = () => {
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
    pizzaElement.setAttribute("class", "pizzaElement")
    
    const pizzaName = document.createElement("p")
    const pizzaIngredients = document.createElement("p")
    const pizzaImg = document.createElement("img")
    pizzaName.innerText = pizza.name
    pizzaName.setAttribute("class", "pizzaName")
    pizzaIngredients.innerText = pizza.ingredients
    pizzaIngredients.setAttribute("class", "pizzaIngredients")
    pizzaImg.setAttribute("src", pizza.picture)
    pizzaImg.setAttribute("class", "pizzaImg")
    pizzaImg.setAttribute("alt", "pizzaImg")

    pizzaElement.appendChild(pizzaImg)
    pizzaElement.appendChild(pizzaName)
    pizzaElement.appendChild(pizzaIngredients)
    PizzaBox.appendChild(pizzaElement)
}

Menu()