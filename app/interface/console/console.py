from app.utilitarios.utils import limpar_console
from app.utilitarios.utils import obter_texto
from app.servicos.servico_cardapio import exibir_cardapio, carregar_cardapio, cadastrar_item, remover_item_cardapio, editar_item_cardapio
from app.servicos.servico_pedidos import criar_pedido
from app.servicos.servico_mesas import cadastrar_mesa, carregar_mesas


def menu_administrativo():
    limpar_console()
    print('\n' + '🔧⚙️ MENU ADMINISTRATIVO ⚙️🔧'.center(50, '='))
    print('=' * 50)
    print('1️⃣  Cadastrar Item no Cardápio')
    print('2️⃣  Editar Item do Cardápio')
    print('3️⃣  Remover Item do Cardápio')
    print('4️⃣  Ver Itens do Cardápio')
    print('5 Adicionar Mesa')
    print('0️⃣  Sair')
    print('=' * 50)
    
    cardapio = carregar_cardapio()
    mesas = carregar_mesas
    
    while True:
        try:
            opcao = int(input('👉 Escolha uma opção: '))
            if opcao in (0, 1, 2, 3, 4, 5,):
                break
            else:
                print('❌ Opção inválida! Digite um número entre (0, 1, 2, 3, 4, 5)')
        except ValueError:
            print('❌ Opção inválida! Digite um número.')
            
    if opcao == 1:
        if cardapio:
            cadastrar_item(cardapio)
    elif opcao == 2:
        if cardapio:
            editar_item_cardapio(cardapio)
    elif opcao == 3:
        if cardapio:
            remover_item_cardapio(cardapio)
            
    elif opcao == 4:
        if cardapio:
            exibir_cardapio()
    
    elif opcao == 5:
        if mesas:
            cadastrar_mesa()

    elif opcao == 0:
        print('\n👋 Até logo! Obrigado por visitar o Café Voyage.\n')    
            
    
def menu_principal():
    limpar_console()
    print('\n' + '☕🍩 BEM-VINDO AO CAFÉ VOYAGE! ☕🍩'.center(50, '='))
    print('=' * 50)
    print('1️⃣  Ver Cardápio')
    print('0️⃣  Sair')
    print('=' * 50)

    cardapio = carregar_cardapio()

    while True:
        try:
            opcao = int(input('👉 Escolha uma opção: '))
            if opcao in (0, 1, 2, 3):
                break
            else:
                print('❌ Opção inválida! Digite um número entre (0, 1, 2, 3)')
        except ValueError:
            print('❌ Opção inválida! Digite um número.')
    
    if opcao == 1:
        exibir_cardapio()
        fazer_pedido = obter_texto("Gostaria de pedir algo? (s/n): ").lower()
        if fazer_pedido not in ['s', 'n']:
            return
        
        if fazer_pedido != 's':
            return
        criar_pedido(cardapio)
        