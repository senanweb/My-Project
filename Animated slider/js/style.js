var slide = document.getElementById ("slidImg")
var images = new Array (
    "Images/naruto.jpg",
    "Images/wall-2.jpg",
    "Images/sunrise.jpg" ,
    "Images/wall.jpg"
                        );
var len = images.length;
var i = 0;
function slider (){
    if(i > len-1) {i =0}
    slide.src = images[i];
    i++
    setTimeout('slider()',3000);
}