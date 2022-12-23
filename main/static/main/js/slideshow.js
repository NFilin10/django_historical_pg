
//Allikas: https://dev.to/coderjay06/how-to-build-a-carousel-from-scratch-531c

const slides = document.getElementsByClassName("carousel-item");
const nextButton = document.getElementById("carousel-button-next");
const prevButton = document.getElementById("carousel-button-prev");
let position = 0;
const numberOfSlides = slides.length;

function hideAllSlides() {
    //eemaldatud kõik slaidid, mida praegu ei vaadata
    for (const slide of slides) {
        slide.classList.remove("carousel-item-visible");
        slide.classList.add("carousel-item-hidden");
    }
}


const handleMoveToNextSlide = function(e) {
    hideAllSlides();

    //kontrollib, kas viimane slaid on näidatud
    if (position === numberOfSlides - 1) {
        position = 0; // läheb tagasi esimese slaidi juurde
    } else {
        //liigub järgmise slaidile
        position++;
    }
    //muudab praegust slaidi nähtavaks
    slides[position].classList.add("carousel-item-visible");
}

const handleMoveToPrevSlide = function(e) {
    hideAllSlides();

    //kontrollib kas oleme praegu esimesel slaidil
    if (position === 0) {
        position = numberOfSlides - 1; //liigub viimase slaidi juurde
    } else {
        //liigub tagasi
        position--;
    }
    //muudab praegust slaidi nähtavaks
    slides[position].classList.add("carousel-item-visible");
}

//kontrollib nuppu vajutamist
nextButton.addEventListener("click", handleMoveToNextSlide);
prevButton.addEventListener("click", handleMoveToPrevSlide);