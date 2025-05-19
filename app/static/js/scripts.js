const optionCards = document.querySelectorAll('.opicao-card');
optionCards.forEach(card => {
    card.addEventListener('click', () => {
        optionCards.forEach(c => c.classList.remove('selected'));
        card.classList.add('selected');
    });
});

const textarea = document.querySelector('.notes-textarea');
const counter = document.querySelector('.character-count');

textarea.addEventListener('input', () => {
    const count = textarea.value.length;
    counter.textContent = `${count}/140`;
});
