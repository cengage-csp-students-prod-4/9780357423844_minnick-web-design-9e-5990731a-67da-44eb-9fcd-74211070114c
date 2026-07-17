/*
    Student Name: Mike Dahlin
    File Name: script.js
    Date: 07/17/2026
*/

//Global variables
var answer = document.querySelector("#answer p");
var heading = document.querySelector("#answer h2");

//Hamburger menu function
function menu() {
    var navlinks = document.getElementById("nav-links");
		var menuicon = document.getElementById("icon");
		if (navlinks.style.display === "block") {
		    navlinks.style.display = "none";
				menuicon.style.color = "#2a1f14";
		} else {
		    navlinks.style.display = "block";
				menuicon.style.color = "#f6eee4";
		}
}

function ans1() {
    heading.innerHTML = "Answer:";
    answer.innerHTML = "Observe the baby animal for several hours. If the mother does not return, contact a wildlife rehabilitator.";
}

function ans2() {
    heading.innerHTML = "Answer:";
    answer.innerHTML = "Signs of rabies include foaming at the mouth, aggressive behavior, and staggering. Do not approach the animal. Contact animal control immediately.";
}

function ans3() {
    heading.innerHTML = "Answer:";
    answer.innerHTML = "No, birds have a poor sense of smell. The parents will not abandon a baby bird if it has been touched by humans. If you find a baby bird, place it back in its nest.";
}

function ans4() {
    heading.innerHTML = "Answer:";
    answer.innerHTML = "Visit our Contact Us page and fill out the form. We will contact you with volunteer opportunities.";
}
