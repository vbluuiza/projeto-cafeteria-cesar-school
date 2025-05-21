// Inicio do código para seleção dos cards dos pedidos | By Lucca 
document.addEventListener('DOMContentLoaded', function() {
    const optionCards = document.querySelectorAll('.opcao-card');
    optionCards.forEach(card => {
        card.addEventListener('click', () => {
            optionCards.forEach(c => c.classList.remove('selected'));
            card.classList.add('selected');
        });
    });
    
    // Contador de caracteres
    const textarea = document.querySelector('.notes-textarea');
    const counter = document.querySelector('.character-count');
    
    textarea.addEventListener('input', () => {
        const count = textarea.value.length;
        counter.textContent = `${count}/140`;
    });
});
// Fim do código para seleção dos cards dos pedidos | By Lucca 
