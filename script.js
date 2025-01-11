// Order Button Click Event
const buttons = document.querySelectorAll('button');

buttons.forEach(button => {
    button.addEventListener('click', () => {
        alert('Thank you for your order! Your food is on its way!');
    });
});