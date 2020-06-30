// gear change setting
var myToggle = document.querySelector(".toggle .fa-cog").onclick = function(){
  this.classList.toggle("fa-spin"); //this for fa
//toggle open
var myOpen = document.querySelector(".box").classList.toggle("open");
}
//change color
const colorLi = document.querySelectorAll (".color li");
colorLi.forEach(li => {
  //for click
  li.addEventListener("click", (e) => { 
      // console.log(e.target.dataset.color) //print code for color
      //set-color
      document.documentElement.style.setProperty('--main--color', e.target.dataset.color);
    });
});
// gear change setting
// ====================== change the background 
let landing = document.querySelector(".land-page");
let myimages = ["../Images/naruto.jpg",
                "../Images/wall-2.jpg",
                "../Images/sunrise.jpg",
                "../Images/wall.jpg"];
setInterval(() => {
 let randomNumber = Math.floor(Math.random()* myimages.length);
 landing.style.backgroundImage = 'url("Images/' + myimages[randomNumber] + '")';
 console.log(randomNumber);
},5000);
// =====================================================