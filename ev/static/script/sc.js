document.addEventListener("DOMContentLoaded", () => {
    const fadeElements = document.querySelectorAll('.fade-in');
    fadeElements.forEach((el, index) => {
        el.style.animationDelay = `${index * 0.5}s`;
    });

    const slideElements = document.querySelectorAll('.slide-in');
    slideElements.forEach((el, index) => {
        el.style.animationDelay = `${index * 0.5}s`;
    });

    const zoomElements = document.querySelectorAll('.zoom-in');
    zoomElements.forEach((el, index) => {
        el.style.animationDelay = `${index * 0.3}s`;
    });
});
