// Function to handle accordion behavior
document.addEventListener("DOMContentLoaded", () => {
  // Get all drop elements
  const drops = document.querySelectorAll(".drop");

  // Add click event listener to each drop header
  document.querySelectorAll(".drop-header").forEach((header) => {
    header.addEventListener("click", function () {
      // Get the parent accordion element
      const currentDrop = this.parentElement;

      // returns if drop is active or not
      const isActive = currentDrop.classList.contains("active");

      // close all other drops
      drops.forEach((drop) => {
        drop.classList.remove("active");
      });

      // If the clicked drop wasn't active before, open it
      if (!isActive) {
        currentDrop.classList.add("active");
      }
    });
  });
});
// When the user scrolls down 20px from the top of the document, show the button
window.onscroll = function () {
  scrollFunction();
};

function scrollFunction() {
  let button = document.getElementById("backToTop");
  if (document.body.scrollTop > 20 || document.documentElement.scrollTop > 20) {
    button.style.display = "block";
  } else {
    button.style.display = "none";
  }
}

// When the user clicks on the button, scroll to the top of the document
function topFunction() {
  document.body.scrollTop = 0; // For Safari
  document.documentElement.scrollTop = 0; // For Chrome, Firefox, IE and Opera
}
