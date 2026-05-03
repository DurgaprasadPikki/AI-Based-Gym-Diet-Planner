let slideIndex = 0;
let iterationCount = 0;
const slides = document.querySelectorAll(".slide");
const maxIterations = 1;
const welcomeScreen = document.getElementById("welcome");
const signupBox = document.getElementById("signup");
const signinBox = document.getElementById("signin");
const detailsForm = document.getElementById("detailsForm");

function showSlides() {
    if (iterationCount >= maxIterations) {
        welcomeScreen.style.opacity = "0";
        setTimeout(() => {
            welcomeScreen.style.display = "none";
            signupBox.style.display = "block";
        }, 2000);
        return;
    }
    slides.forEach((slide) => slide.classList.remove("active"));
    slideIndex++;
    if (slideIndex > slides.length) {
        slideIndex = 1;
        iterationCount++;
    }
    slides[slideIndex - 1].classList.add("active");
    setTimeout(showSlides, 500);
}

function showSignIn() {
    signupBox.style.display = "none";
    signinBox.style.display = "block";
}

function showDetailsForm() {
    signinBox.style.display = "none";
    detailsForm.style.display = "block";
}
function toggleYearsInput() {
    var yearsInput = document.getElementById('yearsExperience');
    var intermediate = document.getElementById('intermediate');
    yearsInput.style.display = intermediate.checked ? 'block' : 'none';
}

showSlides();
