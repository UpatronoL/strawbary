/* Fixed theme.js */
document.addEventListener('DOMContentLoaded', () => {
  const themeToggle = document.getElementById("theme-toggle");
  if (!themeToggle) return;  // safety check

  // Apply saved theme on page load
  const currentTheme = localStorage.getItem("theme") || "light";
  document.body.setAttribute("data-theme", currentTheme);
  themeToggle.textContent = currentTheme === "dark" ? "☀️" : "🌙";

  // Toggle on click
  themeToggle.addEventListener("click", () => {
    const newTheme = document.body.getAttribute("data-theme") === "dark" ? "light" : "dark";
    document.body.setAttribute("data-theme", newTheme);
    localStorage.setItem("theme", newTheme);
    themeToggle.textContent = newTheme === "dark" ? "☀️" : "🌙";
  });
});