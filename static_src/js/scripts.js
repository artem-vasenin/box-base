const drawer = document.getElementById('drawer');
const mobileMenuBtn = document.getElementById('mobile-menu-btn');
const burger = document.getElementById('burger');

mobileMenuBtn.addEventListener('click', (e) => {
   drawer.classList.toggle('drawer--active');
   burger.classList.toggle('burger--active');
});