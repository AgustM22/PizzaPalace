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
    price.innerText = "Price: " + pizza.price
    
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

    ProductBox.appendChild(ProductElement)
}

const PopulateProd = (pizza) => {
    const ProductBox = document.getElementById("ProductBox")

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
    priceSmall.innerText = "Small: " + pizza.pricesmall
    priceMedium.innerText = "Medium: " + pizza.pricemedium
    PriceLarge.innerText = "Large: " + pizza.pricelarge
    
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

    ProductBox.appendChild(ProductElement)
}