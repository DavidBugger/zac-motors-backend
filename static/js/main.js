document.addEventListener("DOMContentLoaded", () => {
  const toggle = document.getElementById("nav-toggle");
  const menu = document.querySelector(".menu");

  toggle.addEventListener("click", () => {
    // Toggle the 'active' class on the menu to show/hide it
    menu.classList.toggle("active");
    // Toggle the 'active' class on the toggle for animation
    toggle.classList.toggle("active");
  });
});

window.addEventListener("scroll", function () {
  const navbar = document.querySelector(".navbar");
  if (window.scrollY > 10) {
    navbar.classList.add("scrolled");
  } else {
    navbar.classList.remove("scrolled");
  }
});

const slides = document.querySelectorAll(".slide");
const points = document.querySelectorAll(".nav-dot");
let index = 0;

function changeSlide(n) {
  slides.forEach((s) => s.classList.remove("active"));
  points.forEach((d) => d.classList.remove("active"));

  slides[n].classList.add("active");
  points[n].classList.add("active");
}

function nextSlide() {
  index = (index + 1) % slides.length;
  changeSlide(index);
}

points.forEach((dot, i) => {
  dot.addEventListener("click", () => {
    index = i;
    changeSlide(i);
  });
});

setInterval(nextSlide, 5000); // Auto-slide every 5s

setInterval(autoSlide, 5000);
// ==================================================
// ===== CAR IMAGE SLIDER BUTTONS =====
const slider = document.getElementById("carSlider");
const slideLeft = document.getElementById("slideLeft");
const slideRight = document.getElementById("slideRight");

// Scroll amount (adjust if needed)
const scrollAmount = 350;

slideRight.addEventListener("click", () => {
  slider.scrollBy({
    left: scrollAmount,
    behavior: "smooth",
  });
});

slideLeft.addEventListener("click", () => {
  slider.scrollBy({
    left: -scrollAmount,
    behavior: "smooth",
  });
});
// =======================================================

const cars = {
  "benz-c300": {
    id: "benz-c300",
    name: "Mercedes Benz 4Matic C300",
    price: "49,950",
    year: 2023,
    color: "Black",
    mileage: "20,360 mi",
    transmission: "Automatic",
    fuel: "Petrol",
    images: [
      "assests/img/benz-c300.jpg",
      "assests/img/benz1.jpg",
      "assests/img/benz2.jpg",
    ],
  },

  "accord-2024": {
    id: "accord-2024",
    name: "Honda Accord 2024",
    price: "32,900",
    year: 2024,
    color: "Grey",
    mileage: "18,000 mi",
    transmission: "Automatic",
    fuel: "Petrol",
    images: [
      "assests/img/accord.jpg",
      "assests/img/accord1.jpg",
      "assests/img/accord2.jpg",
    ],
  },

  "camry-2022": {
    id: "camry-2022",
    name: "Toyota Camry SE 2022",
    price: "29,600",
    year: 2022,
    color: "Blue",
    mileage: "25,000 mi",
    transmission: "Automatic",
    fuel: "Petrol",
    images: ["assests/img/camry.jpg", "assests/img/camry1.jpg"],
  },
};
