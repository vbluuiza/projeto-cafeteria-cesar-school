from app.utils.utilitarios_global import limpar_console
from app.utils.utilitarios_global  import obter_texto

from app.servicos.admin.servico_cardapio_admin import cadastrar_item, remover_item_cardapio, editar_item_cardapio, buscar_item_cardapio
from app.servicos.cliente.servico_cardapio_cliente import exibir_cardapio
from app.servicos.admin.servico_mesas_admin import cadastrar_mesa, carregar_mesas, remover_mesa, buscar_mesa_id

from app.repositorios.repositorio_cardapio import carregar_cardapio
from app.repositorios.repositorio_mesas import carregar_mesas

def menu_funcionario():

    cardapio = carregar_cardapio()
    mesas = carregar_mesas()

    limpar_console()
    print('\n' + '🔧⚙️ MENU FUNCIONÁRIO ⚙️🔧'.center(50, '='))
    print('=' * 50)
    print('1 Fazer pedido')
    print('2 Editar pedido')
    print('3 Cancelar pedido')
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
        if cardapio:
            criar_pedido()
               
    elif opcao == 0:
        print('\n👋 Até logo! \n')    

def menu_administrativo():
    limpar_console()
    print('\n' + '🔧⚙️ MENU ADMINISTRATIVO ⚙️🔧'.center(50, '='))
    print('=' * 50)
    print('1️⃣  Opções de gerenciamento de mesa')
    print('2   Opções de gerenciamento de cardápio')
    print('3   Opções de gerenciamento de pedidos')
    print('0️⃣  Sair')
    print('=' * 50)
    
    while True:
        try:
            opcao = int(input('👉 Escolha uma opção: '))
            if opcao in (0, 1, 2, 3,):
                break
            else:
                print('❌ Opção inválida! Digite um número entre (0, 1, 2, 3)')
        except ValueError:
            print('❌ Opção inválida! Digite um número.')
            
    if opcao == 1:
        menu_administrativo_mesa()
    elif opcao == 2:
        menu_administrativo_cardapio()            
    elif opcao == 0:
        print('\n👋 Até logo!\n') 

def menu_administrativo_mesa():
    limpar_console()
    print('\n' + '🔧⚙️ MENU ADMINISTRATIVO ⚙️🔧'.center(50, '='))
    print('=' * 50)
    print('1 Adicionar Mesa')
    print('2 Remover Mesa')
    print('3 Listar mesas')
    print('4 Editar')
    print('0️⃣  Sair')
    print('=' * 50)
    
    mesas = carregar_mesas()

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
        if mesas:
            cadastrar_mesa()

    elif opcao == 2:
        if mesas:
            remover_mesa()

    elif opcao == 3:
        if mesas:
            buscar_mesa_id()
    elif opcao == 0:
        print('\n👋 Até logo! Obrigado por visitar o Café Voyage.\n')  

def menu_administrativo_cardapio():
    limpar_console()
    print('\n' + '🔧⚙️ MENU ADMINISTRATIVO ⚙️🔧'.center(50, '='))
    print('=' * 50)
    print('1️⃣  Cadastrar Item no Cardápio')
    print('2️⃣  Editar Item do Cardápio')
    print('3️⃣  Remover Item do Cardápio')
    print('4️⃣  Ver Itens do Cardápio')
    print('8 - buscar item cardapio')
    print('0️⃣  Sair')
    print('=' * 50)

    cardapio = carregar_cardapio()

    while True:
        try:
            opcao = int(input('👉 Escolha uma opção: '))
            if opcao in (0, 1, 2, 3, 4, 5, 6, 7, 8):
                break
            else:
                print('❌ Opção inválida! Digite um número entre (0, 1, 2, 3, 4, 5, 6)')
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
            exibir_cardapio(cardapio)
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
            if opcao in (0, 1):
                break
            else:
                print('❌ Opção inválida! Digite um número entre (0, 1)')
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
        