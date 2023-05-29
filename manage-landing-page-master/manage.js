let hamburger_list = document.getElementById("list");
let hamburger_close = document.getElementById("list_close");
let onglets = document.querySelector(".nav_onglets");
let photo = document.querySelector(".avatar");
console.log(photo);
let texte = document.getElementById("texte");
let name = document.getElementById("name");
let checkboxs = Array.from(document.querySelectorAll(".check"));
let label = Array.from(document.getElementsByTagName("label"));
console.log(checkboxs);
console.log(label);
let menu=document.getElementById("landing_img_onglets")
//  apparition de menu
hamburger_list.addEventListener("click", () => {
  hamburger_list.style.display = "none";
  menu.style.height="block";
  hamburger_close.style.display = "block";
  onglets.style.display = "block";
  document.body.classList.add("blur");
});

hamburger_close.addEventListener("click", () => {
  hamburger_close.style.display = "none";
  hamburger_list.style.display = "block";
  menu.style.display="none";

  onglets.style.display = "none";
  document.body.classList.remove("blur");
});
// defilement de carte
label[0].addEventListener("click", () => {
  name.innerText = "Anisha Li";
  photo.innerHTML = '<img src="images/avatar-anisha.png" alt="" id="photo"/>';
  texte.innerText =
    "“Manage has supercharged our team’s workflow.The ability to maintain visibility on larger milestones at all times keeps  everyone motivated  ”";
  texte.className = "resize";
  label[0].style.backgroundColor = "hsl(12, 88%, 59%)";
  label[1].style.backgroundColor = "white";

  label[2].style.backgroundColor = "white";

  label[3].style.backgroundColor = "white";
});
label[1].addEventListener("click", () => {
  name.innerText = "Ali Bravo";
  photo.innerHTML =
    '     <img src="images/avatar-ali.png" alt="" id="photo"/>';
  texte.innerText =
    "“We have been able to cancel so many other subscriptions since using Manage.There is no more cross-channel confusion and everyone is much more focused.”";
  texte.className = "resize";
  label[1].style.backgroundColor = "hsl(12, 88%, 59%)";
  label[0].style.backgroundColor = "white";

  label[2].style.backgroundColor = "white";

  label[3].style.backgroundColor = "white";
});
label[2].addEventListener("click", () => {
  name.innerText = "Richard Watts";
  photo.innerHTML =
    '     <img src="images/avatar-richard.png" alt="" id="photo"/>';
  texte.innerText =
    "“Manage allows us to provide structure and process. It keeps us organized and focused. I can’t stop recommending them to everyone I talk to!”";
  texte.className = "resize";
  label[2].style.backgroundColor = "hsl(12, 88%, 59%)";
  label[1].style.backgroundColor = "white";

  label[0].style.backgroundColor = "white";

  label[3].style.backgroundColor = "white";
});
label[3].addEventListener("click", () => {
  name.innerText = " Shanai Gough";
  photo.innerHTML =
    '     <img src="images/avatar-shanai.png" alt="" id="photo"/>';
  texte.innerText =
    "“Their software allows us to track, manage and collaborate on our projects from anywhere. It keeps the whole team in-sync without being intrusive.”";
  texte.className = "resize";
  label[3].style.backgroundColor = "hsl(12, 88%, 59%)";
  label[2].style.backgroundColor = "white";

  label[1].style.backgroundColor = "white";

  label[0].style.backgroundColor = "white";
});
