
//Autor: Nikita Filin
var popup
var el1

//Funktsioon kontrollib, kas ajutises andmebaasis on midagi või ei ole. Kui on, siis see tähendab, et on vaja näidata popupi
if (localStorage.getItem("blur")) {
    popup = localStorage.getItem("popup")

    el1 =document.getElementById(popup)
    if (el1 != null){
        localStorage.removeItem("blur")
        document.getElementById(popup).style.display = "block"
        const blur_items = document.querySelectorAll('.blur')
        blur_items.forEach(function (blur_item){
            blur_item.style.filter = "blur(8px)"
        })

    }
}