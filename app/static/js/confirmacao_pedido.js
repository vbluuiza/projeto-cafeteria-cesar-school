document.addEventListener('DOMContentLoaded', () => {
    // Simulação: pegar dados
    const pedido = JSON.parse(localStorage.getItem('pedido')) || [];

    const listaItens = document.getElementById('lista-itens');
    const subtotalSpan = document.getElementById('subtotal');
    const totalSpan = document.getElementById('total');

    let subtotal = 0;

    pedido.forEach(item => {
        const li = document.createElement('li');
        li.textContent = `${item.nome} - R$ ${item.preco.toFixed(2)}`;
        listaItens.appendChild(li);
        subtotal += item.preco;
    });

    const taxa = 2.00;
    const total = subtotal + taxa;

    subtotalSpan.textContent = `R$ ${subtotal.toFixed(2)}`;
    totalSpan.textContent = `R$ ${total.toFixed(2)}`;

    document.getElementById('confirmar').addEventListener('click', () => {
        alert('Pedido confirmado!');
        // possivel fetch post
    });
});
