document.addEventListener("DOMContentLoaded", function () {
  let button = document.querySelector("#reminder-button");
  let text = document.querySelector("#reminder-text");

  button.addEventListener("click", function () {
    text.textContent =
      "Keep learning one concept at a time. Strong fundamentals make advanced AI/ML easier.";
  });
});
