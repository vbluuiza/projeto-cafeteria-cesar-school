from app.utils.utilitarios_global import limpar_console, obter_texto, retornar_para_menu

from app.servicos.admin.servico_cardapio import cadastrar_item, remover_item_cardapio, editar_item_cardapio, buscar_item_cardapio
from app.servicos.admin.servico_mesas import cadastrar_mesa, listar_mesas, remover_mesa, buscar_mesa_id, editar_mesa
from app.servicos.admin.servico_pedidos import listar_pedidos
from app.servicos.funcionarios.servico_pedidos import criar_pedido, editar_pedido, remover_pedido

from app.utils.utilitarios_cardapio import exibir_cardapio

from app.repositorios.repositorio_cardapio import carregar_cardapio
from app.repositorios.repositorio_mesas import carregar_mesas
from app.repositorios.repositorio_pedidos import carregar_pedidos


def menu_funcionario():

    pedidos = carregar_pedidos()
    cardapio = carregar_cardapio()
    mesas = carregar_mesas()

    limpar_console()
    print('\n' + '🔧⚙️ MENU FUNCIONÁRIO ⚙️🔧'.center(50, '='))
    print('=' * 50)
    print('1️⃣  Fazer pedido')
    print('2️⃣  Editar pedido')
    print('3️⃣  Cancelar pedido')
    print('4️⃣  Voltar')
    print('0️⃣  Sair')
    print('=' * 50)

    while True:
        try:
            opcao = int(input('👉 Escolha uma opção: '))
            if opcao in (0, 1, 2, 3, 4):
                break
            else:
                print('❌ Opção inválida! Digite um número entre (0, 1, 2, 3, 4)')
        except ValueError:
            print('❌ Opção inválida! Digite um número.')
            
    if opcao == 1:
        if cardapio:
            criar_pedido(cardapio,pedidos,mesas)

    elif opcao == 2:
        editar_pedido(cardapio,pedidos,mesas)
    
    elif opcao == 3:
        remover_pedido(pedidos)

    elif opcao == 4:
        retornar_para_menu()

    elif opcao == 0:
        print('\n👋 Até logo! \n')    

def menu_administrativo():
    limpar_console()
    print('\n' + '🔧⚙️ MENU ADMINISTRATIVO ⚙️🔧'.center(50, '='))
    print('=' * 50)
    print('1️⃣  Opções de gerenciamento de mesa')
    print('2️⃣  Opções de gerenciamento de cardápio')
    print('3️⃣  Opções de gerenciamento de pedidos')
    print('4️⃣  Voltar')
    print('0️⃣  Sair')
    print('=' * 50)
    
    while True:
        try:
            opcao = int(input('👉 Escolha uma opção: '))
            if opcao in (0, 1, 2, 3, 4):
                break
            else:
                print('❌ Opção inválida! Digite um número entre (0, 1, 2, 3, 4)')
        except ValueError:
            print('❌ Opção inválida! Digite um número.')
            
    if opcao == 1:
        menu_administrativo_mesa()
    elif opcao == 2:
        menu_administrativo_cardapio()     
    elif opcao == 3:
        menu_administrativo_pedidos()
    elif opcao == 4:
        retornar_para_menu()       
    elif opcao == 0:
        print('\n👋 Até logo!\n') 

def menu_administrativo_mesa():
    limpar_console()
    print('\n' + '🔧⚙️ MENU ADMINISTRATIVO ⚙️🔧'.center(50, '='))
    print('=' * 50)
    print('1️⃣  Adicionar Mesa')
    print('2️⃣  Remover Mesa')
    print('3️⃣  Buscar Mesa')
    print('4️⃣  Listar Mesas')
    print('5️⃣  Editar Mesa')
    print('6️⃣  Voltar')
    print('0️⃣  Sair')
    print('=' * 50)
    
    mesas = carregar_mesas()

    while True:
        try:
            opcao = int(input('👉 Escolha uma opção: '))
            if opcao in (0, 1, 2, 3, 4, 5, 6):
                break
            else:
                print('❌ Opção inválida! Digite um número entre (0, 1, 2, 3, 4, 5)')
        except ValueError:
            print('❌ Opção inválida! Digite um número.')
            
    if opcao == 1:
        if mesas:
            cadastrar_mesa(mesas)

    elif opcao == 2:
        if mesas:
            remover_mesa(mesas)

    elif opcao == 3:
        if mesas:
            buscar_mesa_id(mesas)
            
    elif opcao == 4:
        if mesas:
            listar_mesas(mesas)
    
    elif opcao == 5:
        editar_mesa(mesas)
    
    elif opcao == 6:
        menu_administrativo()
        
            
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
    print('5️⃣  Buscar item cardapio')
    print('6️⃣  Voltar')
    print('0️⃣  Sair')
    print('=' * 50)

    cardapio = carregar_cardapio()

    while True:
        try:
            opcao = int(input('👉 Escolha uma opção: '))
            if opcao in (0, 1, 2, 3, 4, 5, 6):
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
            exibir_cardapio()
    elif opcao == 5:
        if cardapio:
            buscar_item_cardapio(cardapio)
    elif opcao == 6:
        menu_administrativo()
    elif opcao == 0:
        print('\n👋 Até logo! Obrigado por visitar o Café Voyage.\n') 

def menu_administrativo_pedidos():

    pedidos = carregar_pedidos()
    cardapio = carregar_cardapio()
    mesas = carregar_mesas()

    limpar_console()
    print('\n' + '🔧⚙️ MENU ADMINISTRATIVO ⚙️🔧'.center(50, '='))
    print('=' * 50)
    print('1️⃣  Listar todos os pedidos')
    print('2️⃣  Voltar')
    print('0️⃣  Sair')
    print('=' * 50)

    while True:
        try:
            opcao = int(input('👉 Escolha uma opção: '))
            if opcao in (0, 1, 2):
                break
            else:
                print('❌ Opção inválida! Digite um número entre (0, 1, 2)')
        except ValueError:
            print('❌ Opção inválida! Digite um número.')

    if opcao == 1:
        listar_pedidos(cardapio,pedidos,mesas)
    elif opcao == 2:
        menu_administrativo()