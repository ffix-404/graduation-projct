// Function to show an alert dialog
// script.js
// script.js
document.addEventListener('DOMContentLoaded' , function(){
    document.querySelector('form').onsubmit=function(input){
        input.preventDefault()
        const  color = document.querySelector("#color");
       const h1 = document.querySelector("h1")
       h1.style.color = color.value
    };
});


