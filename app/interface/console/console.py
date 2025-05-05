from app.utilitarios.utils import limpar_console
from app.servicos.servico_cardapio import exibir_cardapio, carregar_cardapio, cadastrar_item
    
def menu_administrativo():
    limpar_console()
    print('\n' + '🔧⚙️ MENU ADMINISTRATIVO ⚙️🔧'.center(50, '='))
    print('=' * 50)
    print('1️⃣  Cadastrar Item no Cardápio')
    print('2️⃣  Editar Item do Cardápio')
    print('3️⃣  Remover Item do Cardápio')
    print('4️⃣  Ver Itens do Cardápio')
    print('0️⃣  Sair')
    print('=' * 50)
    
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
        cardapio = carregar_cardapio()
        if cardapio:
            cadastrar_item(cardapio)

    
def menu_principal():
    limpar_console()
    print('\n' + '☕🍩 BEM-VINDO AO CAFÉ VOYAGE! ☕🍩'.center(50, '='))
    print('=' * 50)
    print('1️⃣  Ver Cardápio')
    print('2️⃣  Fazer Pedido')
    print('3️⃣  Ver Status do Pedido')
    print('0️⃣  Sair')
    print('=' * 50)
    
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


