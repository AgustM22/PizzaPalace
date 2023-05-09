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
        pizza.setAttribute("class", "PizzaOrderName")
        
        pizza.innerText = PizzaName
        quantity.innerText = 1

        const OrderBox = document.getElementById("OrderBox")

        OrderSelect.appendChild(pizza)
        OrderSelect.appendChild(quantity)
        OrderBox.appendChild(OrderSelect)
    }
}

const ClearOrder = () => {
    TfoCount = 0
    const OrderBox = document.getElementById("OrderBox")
    OrderBox.innerHTML = ""
}

const AddToCart = async (num) => {
    if (num == 1) {
        // Offers
        const OfferId = document.getElementById("OfferText").getAttribute("name");
        const DataDict = {}
        DataDict["type"] = "offer"

        const items = document.getElementsByClassName("PizzaOrderName")
        const itemArray = []
        items.forEach((item) => {
            itemArray.push(item.innerHTML)
        })
        
        DataDict["item"] = itemArray
        DataDict["price"] = document.getElementById("FullPrice").innerHTML;
        DataDict["name"] = document.getElementById("OfferText").innerHTML;
        DataDict["qty"] = 1;
        const response = await axios("/cart/addcart", {params: DataDict})
    }
    else {
        // Pizzas
        const PizzaTitle = document.getElementById("PizzaTitle").textContent
        const Price = document.getElementById("FullPrice").textContent
        const Toppings = Array.from(document.getElementsByClassName("AdditionalToppings"))
        let AdditionalToppings = ""

        Toppings.forEach((topping) => {
            AdditionalToppings += topping.id + ", "
        })
        AdditionalToppings = AdditionalToppings.slice(0, -2)
        const response = await axios("/cart/addcart", {params: {"type": "pizza", "name": PizzaTitle, "price": Price, "qty": 1, "additionaltoppings": AdditionalToppings}})
    }
}

const DisplayCart = async () => {
    const response = await axios("/cart/getcart")
    console.log(response.data)
}

const DeleteCart = async () => {
    const response = await axios("/cart/deletecart")
    console.log(response.data)
}

const ChangePizzaTopping = (checkbox) => {
    if (checkbox.checked) {
        const OrderBox = document.getElementById("OrderBox")
        const ToppingDetails = checkbox.value.split("+")

        const topping = document.createElement("p")
        topping.setAttribute("class", "AdditionalToppings")
        topping.setAttribute("id", ToppingDetails[0])
        topping.setAttribute("value", ToppingDetails[1].slice(0, -2))

        topping.innerHTML = "+ " + ToppingDetails[0]
        OrderBox.appendChild(topping)
        ChangePrice()
    }
    else {
        const ToppingDetails = checkbox.value.split("+")
        const topping = document.getElementById(ToppingDetails[0])
        topping.parentNode.removeChild(topping)
        ChangePrice()
    }
}

const ChangePrice = () => {
    const OrderBoxChildren = Array.from(document.getElementById("OrderBox").children)
    let TotalPrice = 0

    OrderBoxChildren.forEach((child) => {
        TotalPrice += parseInt(child.attributes.value.value)    
    })

    const PriceElem = document.getElementById("FullPrice")
    PriceElem.innerText = TotalPrice + "Kr."
}