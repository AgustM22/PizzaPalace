// Stuff for Menu
const SearchFilter = async () => {
    const Filter = document.getElementById("search").value
    const response = await axios("/menu/filter", {params: {"filter": Filter}})

    const Pizzadict = response.data

    const Main = document.getElementById("ProductBox")
    Main.innerHTML = ""

    Pizzadict.forEach((pizza) => {
        PopulateProd(pizza)
    })
}

const SearchOfferFilter = async () => {
    const Filter = document.getElementById("search").value
    const response = await axios("/offer/filter", {params: {"filter": Filter}})

    const Offerdict = response.data

    const Main = document.getElementById("ProductBox")
    Main.innerHTML = ""

    Offerdict.forEach((offer) => {
        PopulateOfferBox(offer)
    })
}

const PopulateOfferBox = (pizza) => {
    const ProductBox = document.getElementById("ProductBox")

    const ProductLink = document.createElement("a")
    ProductLink.setAttribute("href", pizza.id)

    const ProductElement = document.createElement("div")
    const ProductText = document.createElement("div")
    const ProductPrices = document.createElement("div")
    ProductElement.setAttribute("class", "ProductElement")
    ProductText.setAttribute("class", "ProductText")
    ProductPrices.setAttribute("class", "ProductPrices")
    
    const ProductName = document.createElement("h1")
    const ProductDesc = document.createElement("p")
    const ProductImg = document.createElement("img")

    const price = document.createElement("p")
    price.innerText = "Price: " + pizza.price + "Kr."
    
    ProductName.innerText = pizza.name
    ProductName.setAttribute("class", "ProductName")
    ProductDesc.innerText = pizza.description
    ProductDesc.setAttribute("class", "ProductIngredients")

    ProductImg.setAttribute("src", pizza.pic)
    ProductImg.setAttribute("class", "ProductImg")
    ProductImg.setAttribute("alt", "ProductImg")

    ProductElement.appendChild(ProductImg)

    ProductText.appendChild(ProductName)
    ProductText.appendChild(ProductDesc
)
    ProductElement.appendChild(ProductText)

    ProductPrices.appendChild(price)
    ProductElement.appendChild(ProductPrices)

    ProductLink.appendChild(ProductElement)
    ProductBox.appendChild(ProductLink)
}

const PopulateProd = (pizza) => {
    const ProductBox = document.getElementById("ProductBox")

    const ProductLink = document.createElement("a")
    ProductLink.setAttribute("href", pizza.id)

    const ProductElement = document.createElement("div")
    const ProductText = document.createElement("div")
    const ProductPrices = document.createElement("div")
    ProductElement.setAttribute("class", "ProductElement")
    ProductText.setAttribute("class", "ProductText")
    ProductPrices.setAttribute("class", "ProductPrices")
    
    const ProductName = document.createElement("h1")
    const ProductIngredients = document.createElement("p")
    const ProductImg = document.createElement("img")

    const priceSmall = document.createElement("p")
    const priceMedium = document.createElement("p")
    const PriceLarge = document.createElement("p")
    priceSmall.innerText = "Small: " + pizza.pricesmall + "Kr."
    priceMedium.innerText = "Medium: " + pizza.pricemedium + "Kr."
    PriceLarge.innerText = "Large: " + pizza.pricelarge + "Kr."
    
    ProductName.innerText = pizza.name
    ProductName.setAttribute("class", "ProductName")
    ProductIngredients.innerText = pizza.toppings
    ProductIngredients.setAttribute("class", "ProductIngredients")

    ProductImg.setAttribute("src", pizza.pic)
    ProductImg.setAttribute("class", "ProductImg")
    ProductImg.setAttribute("alt", "ProductImg")

    ProductElement.appendChild(ProductImg)

    ProductText.appendChild(ProductName)
    ProductText.appendChild(ProductIngredients)
    ProductElement.appendChild(ProductText)

    ProductPrices.appendChild(priceSmall)
    ProductPrices.appendChild(priceMedium)
    ProductPrices.appendChild(PriceLarge)
    ProductElement.appendChild(ProductPrices)

    ProductLink.appendChild(ProductElement)
    ProductBox.appendChild(ProductLink)
}

let TfoCount = 0 

const AddPizzaToOrder = (PizzaName) => {
    if (TfoCount != 2) {
        TfoCount++;

        const pizza = document.createElement("p")
        const quantity = document.createElement("p")
        const OrderSelect = document.createElement("div")

        OrderSelect.setAttribute("class", "OrderSelect")
        pizza.innerText = PizzaName
        quantity.innerText = 1

        const OrderBox = document.getElementById("OrderBox")

        OrderSelect.appendChild(pizza)
        OrderSelect.appendChild(quantity)
        OrderBox.appendChild(OrderSelect)

        // Can add more functionality to save the pizzas selected into an array and send that into cart as an object methinks
        // Also remember to reset TfoCount on cart press
    }
}

const ClearOrder = () => {
    TfoCount = 0
    const OrderBox = document.getElementById("OrderBox")
    OrderBox.innerHTML = ""
}