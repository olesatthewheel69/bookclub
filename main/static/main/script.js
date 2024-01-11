const links = document.querySelectorAll("nav ul li a");

links.forEach((link) => {
    link.addEventListener("mouseover", () => {
        link.style.transform = "rotate(10deg)"; /* Apply the desired rotation value */
    });

    link.addEventListener("mouseout", () => {
        link.style.transform = "rotate(0)"; /* Reset the rotation on mouseout */
    });
});