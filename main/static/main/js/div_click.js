
//Autor: Nikita Filin
var el
//Funktsioon lisab ajutisse andmebaasi infot, kas oli vajutatud div plokk, selleks et kuvada popupi
function popup(element, html, popup) {
    el = document.getElementById(element)
    if (el!=null){
        el.onclick = function () {
            localStorage.setItem("blur", "yes")
            localStorage.setItem("popup", popup)
            document.location.href = html;
        }
    }
}