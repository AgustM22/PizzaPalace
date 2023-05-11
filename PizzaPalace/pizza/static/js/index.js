// Stuff for Menu
const SearchFilter = async () => {
    const Filter = document.getElementById("Search").value
    const VegeterianFilter = document.getElementById("VegeterianCheck").checked
    const SpicyFilter = document.getElementById("SpicyCheck").checked
    const SortSelect = document.getElementById("SortSelect").value

    const response = await axios("/menu/filter", {params: {"filter": Filter, "veg": VegeterianFilter, "spicy": SpicyFilter, "sort": SortSelect}})
    const Pizzadict = response.data

    const Main = document.getElementById("ProductBox")
    Main.innerHTML = ""

    Pizzadict.forEach((pizza) => {
        PopulateProd(pizza)
    })
}

const SearchOfferFilter = async () => {
    const Filter = document.getElementById("Search").value
    const SortSelect = document.getElementById("SortOfferSelect").value

    const response = await axios("/offer/filter", {params: {"filter": Filter, "sort": SortSelect}})

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
    const ProductHighLight = document.createElement("div")
    const ProductPrices = document.createElement("div")

    ProductElement.setAttribute("class", "ProductElement")
    ProductText.setAttribute("class", "ProductText")
    ProductPrices.setAttribute("class", "ProductPrices")
    ProductHighLight.setAttribute("class", "ProductHighLight")
    
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
    ProductHighLight.appendChild(ProductName)
    ProductText.appendChild(ProductHighLight)
    ProductText.appendChild(ProductIngredients)
    ProductElement.appendChild(ProductText)



    if (pizza.veg === true) {
        const VegetarianImg = document.createElement("img")
        VegetarianImg.setAttribute("src", "/static/images/veg.png")
        VegetarianImg.setAttribute("class", "VegeterianPic")
        VegetarianImg.setAttribute("alt", "Vegeterian!")
        ProductHighLight.appendChild(VegetarianImg)
    }
    if (pizza.spicy === true) {
        const SpicyImg = document.createElement("img")
        SpicyImg.setAttribute("src", "/static/images/fire.png")
        SpicyImg.setAttribute("class", "SpicyPic")
        SpicyImg.setAttribute("alt", "Spicy!")
        ProductHighLight.appendChild(SpicyImg)
    }


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
        const DataDict = {}
        const items = Array.from(document.getElementsByClassName("PizzaOrderName"))
        let itemString = ""
        items.forEach((item) => {
            itemString += (item.innerHTML) + ", "
        })
        
        DataDict["type"] = "offer"
        DataDict["item"] = itemString
        DataDict["price"] = document.getElementById("FullPrice").innerHTML.slice(0, -3);
        DataDict["name"] = document.getElementById("OfferTitle").innerText;
        DataDict["qty"] = 1;
        DataDict["img"] = document.getElementById("OfferPic").src;
        
        if ((document.getElementById("OfferText").getAttribute("name")) == 1) {
            // Two For one Offer
            if (TfoCount === 2) {
                const response = await axios("/cart/addcart", {params: DataDict});
                history.go(-2);
                }
            else {
                alert("You must select two pizzas!")
                }
            }
        else {
            // Hottest Pizzas Offer
            const response = await axios("/cart/addcart", {params: DataDict});
            history.go(-1);
        }
    }
    else {
        // Pizzas
        const PizzaTitle = document.getElementById("PizzaTitle").textContent
        const PizzaSize = document.getElementById("SizeBox").getAttribute("value")
        const Price = document.getElementById("FullPrice").textContent.slice(0, -3);
        const PizzaSrc = document.getElementById("PizzaPic").src;
        const Toppings = Array.from(document.getElementsByClassName("AdditionalToppings"))
        let AdditionalToppings = PizzaSize + ". "

        Toppings.forEach((topping) => {
            AdditionalToppings += topping.innerText + " "
        })
        const response = await axios("/cart/addcart", {params: {"type": "pizza", "name": PizzaTitle, "price": Price, "qty": 1, "additionaltoppings": AdditionalToppings, "img": PizzaSrc}})
    }
}

const ChangePizzaTopping = (checkbox) => {
    if (checkbox.checked) {
        const OrderSelect = document.getElementById("OrderSelect")
        const ToppingDetails = checkbox.value.split("+")
        if (ToppingDetails[2] == "set") {
            const topping = document.getElementById(ToppingDetails[0])
            topping.parentNode.removeChild(topping)
        }
        else {    
            const topping = document.createElement("label")
            topping.setAttribute("class", "AdditionalToppings")
            topping.setAttribute("id", ToppingDetails[0])
            topping.setAttribute("value", ToppingDetails[1].slice(0, -2))
            
            topping.innerHTML = "+ " + ToppingDetails[0]
            OrderSelect.appendChild(topping)
            ChangePrice()
        }
    }
    else {
        const ToppingDetails = checkbox.value.split("+")
        if (ToppingDetails[2] == "set") {
            const topping = document.createElement("label")
            topping.setAttribute("class", "AdditionalToppings")
            topping.setAttribute("id", ToppingDetails[0])
            topping.setAttribute("value", ToppingDetails[1].slice(0, -2))
            topping.innerHTML = "- " + ToppingDetails[0]
            OrderSelect.appendChild(topping)
        }
        else {
            const topping = document.getElementById(ToppingDetails[0])
            topping.parentNode.removeChild(topping)
            ChangePrice()
        }
    }
}

const EditPizzaValue = (newprice) => {
    const SizeBox = document.getElementById("SizeBox")
    const PizzaValue = document.getElementById("OrderSelect")
    const Values = newprice.split('+')
    SizeBox.setAttribute("value", Values[0])
    PizzaValue.setAttribute("value", parseInt(Values[1]))
    ChangePrice()
}

const ChangePrice = () => {
    const OrderSelectChildren = Array.from(document.getElementById("OrderSelect").children)
    let TotalPrice = parseInt(document.getElementById("OrderSelect").getAttribute("value"))

    OrderSelectChildren.forEach((child) => {
        TotalPrice += parseInt(child.attributes.value.value)    
    })

    const PriceElem = document.getElementById("FullPrice")
    PriceElem.innerText = TotalPrice + "Kr."
}

const EditValue = async (keyword, ID) => {
    const ProductBox = document.getElementById("product" + ID)
    const CartBox = document.getElementById("cart" + ID)
    const PriceBox = document.getElementById("price" + ID)
    const Value = document.getElementById("value" + ID)
    const Quantity = document.getElementById("qty" + ID)
    const DetailArray = ID.split("=")
    let CartValue = CartBox.getAttribute("value").split("=")

    if (keyword == 'del') {
        ProductBox.remove()
        CartBox.remove()
        PriceBox.remove()
        Quantity.remove()
        FixPrice()
        return await axios("/cart/editcart", {params: {"remove": true, "name": DetailArray[0], "qty": Value.value, "price": CartValue[1], "extra":DetailArray[1]}})
    }
    else if (keyword == 'reduce') {
        if (Value.value <= 1) {
            ProductBox.remove()
            CartBox.remove()            
            PriceBox.remove()
            Quantity.remove()
            FixPrice()
            return await axios("/cart/editcart", {params: {"remove": true, "name": DetailArray[0], "qty": Value.value, "price": CartValue[1], "extra":DetailArray[1]}})
        }
        else {
            CartBox.setAttribute("value", (Value.value - 1) + "=" + CartValue[1])
            Quantity.textContent = (Value.value - 1)        
            Value.value = Value.value - 1
            Value.setAttribute("value", (Value.value))
        }
    }
    else if (keyword == 'add') {
        CartBox.setAttribute("value", (parseInt(Value.value) + 1) + "=" + CartValue[1])
        Quantity.textContent = (parseInt(Value.value) + 1)        
        Value.value = (parseInt(Value.value) + 1)
        Value.setAttribute("value", (parseInt(Value.value)))
    }
    else if (keyword == 'change') {
        if (isNaN(Value.value)) {
            // Pass
        }
        else if (Value.value < 1) {
            ProductBox.remove()
            CartBox.remove()
            PriceBox.remove()
            Quantity.remove()
            FixPrice()
            return await axios("/cart/editcart", {params: {"remove": true, "name": DetailArray[0], "qty": Value.value, "price": CartValue[1], "extra":DetailArray[1]}})
        }
        else {
            CartBox.setAttribute("value", (Value.value) + "=" + CartValue[1])
            Quantity.textContent = (Value.value)        
            Value.setAttribute("value", (Value.value))
        }
    }
    FixPrice()
    return await axios("/cart/editcart", {params: {"remove": false, "name": DetailArray[0], "qty": Value.value, "price": CartValue[1], "extra":DetailArray[1]}})
}

const FixPrice = () => {
    const FullPrice = document.getElementById("CheckoutPrice")
    const AllPrices = Array.from(document.getElementsByClassName("SingleElementPrice"))
    const AllQuantities = Array.from(document.getElementsByClassName("SingleElementQuantity"))
    let TotalPrice = 0

    AllPrices.forEach((item, index) => {
        let text = item.textContent
        let temp = parseInt(text.slice(0, -3)) * parseInt(AllQuantities[index].textContent)
        TotalPrice += temp
    })

    FullPrice.textContent = (TotalPrice + "Kr.")
}

const ClearCart = async () => {
    const AllNames = document.getElementsByClassName("SingleElementName")
    const AllQuantities = document.getElementsByClassName("SingleElementQuantity")
    const AllPrices = document.getElementsByClassName("SingleElementPrice")
    const FullPrice = document.getElementById("CheckoutPrice")
    const AllProducts = document.getElementsByClassName("CartProduct")

    while(AllNames.length > 0){
        AllNames[0].parentNode.removeChild(AllNames[0]);
    }

    while(AllQuantities.length > 0){
        AllQuantities[0].parentNode.removeChild(AllQuantities[0]);
    }

    while(AllPrices.length > 0){
        AllPrices[0].parentNode.removeChild(AllPrices[0]);
    }

    while(AllProducts.length > 0){
        AllProducts[0].parentNode.removeChild(AllProducts[0]);
    }

    FullPrice.textContent = ("0Kr.")
    return await axios("/cart/editcart", {params: {"wipe": true}})
}