// ================================
let landing = document.querySelector('.images');
let myimages = ['3.jpg','4.jpg','5.jpg','6.jpg'];
setInterval(() => {
  let randomNumber = Math.floor(Math.random() * myimages.length);
  console.log (myimages[randomNumber])
  landing.style.backgroundImage ='url ("../P-2/Images' + myimages[randomNumber] + '")';
}, 1000);
// =================================================
// var landing = document.querySelector('.images');
//     myimages = ['3.jpg','4.jpg','5.jpg','6.jpg'];
    
// function ChangeImage(landing, myimages) {
//     'use strict';
//     setInterval (function () {
//       var randomNumber = Math.floor(Math.random() * myimages.length);
//       console.log (myimages[randomNumber])
//       landing.src = myimages[randomNumber];
//     }, 1000);
// }  
// ChangeImage (landing, myimages)
// //  console.log (myimages[randomNumber])