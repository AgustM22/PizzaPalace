const Menu = () => {
    const Main = document.getElementById("MainBlock")
    Main.innerHTML = ""

    const SearchBar = document.createElement("div")
    const Search = document.createElement("input")
    const PizzaText = document.createElement("p")
    const Sliders = document.createElement("img")

    SearchBar.setAttribute("id", "SearchBar")
    Search.setAttribute("placeholder", "Search...")
    PizzaText.innerText = "Pizza"
    Sliders.setAttribute("alt", "Settings")
    Sliders.setAttribute("src", "/static/images/sliders.svg")

    SearchBar.appendChild(Search)
    SearchBar.appendChild(PizzaText)
    SearchBar.appendChild(Sliders)
    Main.appendChild(SearchBar)
}

Menu()