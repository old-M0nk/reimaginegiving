function openModal() {
  document.getElementById('myModal').style.display = "block";
  document.getElementsByTagName("body")[0].style.position = "fixed";
}

function closeModal() {
  document.getElementById('myModal').style.display = "none";
  document.getElementsByTagName("body")[0].style.position = "";
}

var slideIndex = 1;
showSlides(slideIndex);

function plusSlides(n) {
  showSlides(slideIndex += n);
}

function currentSlide(n) {
  showSlides(slideIndex = n);
}

function showSlides(n) {
  var i;
  var slides = document.getElementsByClassName("myGallerySlides");
  var dots = document.getElementsByClassName("myGallerydemo");
  var captionText = document.getElementById("myGalleryCcaption");
  if (n > slides.length) {slideIndex = 1}
  if (n < 1) {slideIndex = slides.length}
  for (i = 0; i < slides.length; i++) {
      slides[i].style.display = "none";
  }
  for (i = 0; i < dots.length; i++) {
      dots[i].className = dots[i].className.replace(" activeImage", "");
  }
  slides[slideIndex-1].style.display = "block";
  dots[slideIndex-1].className += " activeImage";
  captionText.innerHTML = dots[slideIndex-1].alt;
}