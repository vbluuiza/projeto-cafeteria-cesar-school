from app.utils.utilitarios_global import limpar_console, retorno_main

def listar_pedidos(cardapio, pedidos, mesas):
    limpar_console()
    
    print('\n' + ' LISTA DOS PEDIDOS '.center(50, '='))
    print("")

    pedidos_dados = pedidos['pedidos']
    if not pedidos_dados:
        print("❌ Não há pedidos ativos no momento.")
        return
    
    print("📋 Mesas com pedidos ativos:")
    for pedido in pedidos_dados:
        print(f"\n➤ Mesa: {pedido['mesa']}")
        print("-" * 40)
        print(f"🍽️  Itens: {', '.join(pedido['itens'])}")
        print(f"📝 Observações: {pedido.get('observacoes', 'Nenhuma')}")
        print(f"📌 Status: {pedido.get('status', 'Sem status')}")
        print("-" * 40)
        
    retorno_main()