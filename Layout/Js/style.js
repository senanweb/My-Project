var slide1 = document.getElementById("layout1");
var slide2 = document.getElementById("layout2");
var slide3 = document.getElementById("layout3");
var btn1 = document.getElementById("btn1");
var btn2 = document.getElementById("btn2");
var btn3 = document.getElementById("btn3");


function openHtml() {
    slide1.style.transform = "translateX(0)";
    slide2.style.transform = "translateX(100%)";
    slide3.style.transform = "translateX(100%)";
    btn1.style.color = "#ff7846";
    btn2.style.color = "#000";
    btn3.style.color = "#000";
    slide1.style.transitionDelay = "0.4s";
    slide2.style.transitionDelay = "0s";
    slide3.style.transitionDelay = "0s";
}
// end html
function openCss() {
    slide1.style.transform = "translateX(100%)";
    slide2.style.transform = "translateX(0)";
    slide3.style.transform = "translateX(100%)";
    btn1.style.color = "#000";
    btn2.style.color = "#ff7846";
    btn3.style.color = "#000";
    slide1.style.transitionDelay = "0s";
    slide2.style.transitionDelay = "0.4s";
    slide3.style.transitionDelay = "0s";
}
// end css
function openJs() {
    slide1.style.transform = "translateX(100%)";
    slide2.style.transform = "translateX(100%)";
    slide3.style.transform = "translateX(0)";
    btn1.style.color = "#000";
    btn2.style.color = "#000";
    btn3.style.color = "#ff7846";
    slide1.style.transitionDelay = "0s";
    slide2.style.transitionDelay = "0s";
    slide3.style.transitionDelay = "0.4s";
}