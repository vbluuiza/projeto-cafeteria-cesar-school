import json

from app.utils.utilitarios_global import limpar_console, retorno_main

from app.utils.utilitarios_global import obter_texto, obter_int
from app.utils.utilitarios_global import STATUS_PEDIDO, STATUS_MESA


def criar_pedido(cardapio:dict, pedidos:dict, mesas:dict):
    limpar_console()
    
    while True:
        total_de_mesas = mesas['total_de_mesas']
        mesa_em_atendimento = obter_int("🔢 Informe o número da mesa atendida: ", 'O número da mesa não pode ser negativo. Tente novamente.')

        if mesa_em_atendimento > total_de_mesas:
            print(f"❌ Mesa inexistente. Mesas disponíveis: de 1 até {total_de_mesas}.")
            return

        mesas_indisponiveis = [pedido['mesa'] for pedido in pedidos['pedidos']]
        if mesa_em_atendimento in mesas_indisponiveis:
            print(f'Mesa {mesa_em_atendimento} ocupada. Escolha outra mesa.\n')
            continue
        else: 
            break
            
    exibir_cardapio()

    print("\n========== ☕ PEDIDO NOVO ☕ ==========")
    print("+📌 Escolha os itens que deseja adicionar ao pedido:")


    itens_cardapio = {
        item['nome']: item['preco']
        for categoria in cardapio.values() for subcategoria in categoria.values() for item in subcategoria
    }

    itens_pedidos = []
    conta = []
    while True:
        pedido = obter_texto("\n🍽️  Digite o nome do item: ")

        if pedido not in itens_cardapio:
            print("❌ Item não encontrado no cardápio. Tente novamente.")
            continue

        itens_pedidos.append(pedido)
        conta.append(itens_cardapio[pedido])
        print(f"✅ Item '{pedido}' adicionado com sucesso!")
        
        adicionar_item = obter_texto("\n➕ Deseja adicionar mais algum item? (s/n): ").lower()
        if adicionar_item == 'n':
            break
        if adicionar_item == 's':
            continue
        
    if not itens_pedidos:
        print("\n⚠️ Nenhum item foi adicionado ao pedido. Cancelando operação.")
        return
    
    observacao = obter_texto("\n🗒️ Deseja adicionar alguma observação ao pedido?: ")
    if observacao == '':
        observacao = 'Nenhuma'

    soma_conta = sum(conta)
    conta_final = soma_conta

    pedido = {
        'mesa': mesa_em_atendimento,
        'itens': itens_pedidos,
        'preco_total': conta_final,
        'observacoes': observacao,
        'status': STATUS_PEDIDO[0]
    }
    
    for mesa in mesas['lista_de_mesas']:
        if mesa['id'] == mesa_em_atendimento:
            print(f'MESA NO ID{mesa['id']} | MESAS: {mesa}')
            mesa['status'] = STATUS_MESA[1]
            salvar_mesas(mesas)
        
    pedidos['pedidos'].append(pedido)
    pedidos["total_pedidos"] += 1
    salvar_pedidos(pedidos)
    
    limpar_console()
    
    print("\n🎉 Pedido registrado com sucesso!")
    print(f"📍 Mesa: {mesa_em_atendimento}")
    print("🧾 Itens do pedido:")
    for item in itens_pedidos:
        print(f"   ➤ {item}")
    print(f"Total: R${conta_final}")
    print(f"📦 Status inicial: {STATUS_PEDIDO[0]}")

    retorno_main()

def editar_pedido(cardapio, pedidos, mesas):
    limpar_console()
    
    exibir_cardapio()

    print ("========== ☕ EDITAR PEDIDO ☕ ==========")

    pedidos_dados = pedidos['pedidos']
    if not pedidos_dados:
        print("❌ Não há pedidos ativos no momento.")
        return
    
    print("\n📋 Mesas com pedidos ativos:")
    for pedido in pedidos_dados:
        print(f"   ➤ Mesa {pedido['mesa']}")
    
    mesa_selecionada = obter_int("\n🔢 Informe o número da mesa selecionada: ", '⚠️ O número da mesa não pode ser negativo. Tente novamente.')
    
    pedido = next((pedido for pedido in pedidos_dados if pedido['mesa'] == mesa_selecionada), None)
    
    if not pedido:
        print("⚠️ Mesa não encontrada com pedido ativo.")
        return
    
    print(f"\n📦 Pedido atual da mesa {mesa_selecionada}:")
    print("-" * 40)
    print(f"🍽️  Itens: {', '.join(pedido['itens'])}")
    print(f"📝 Observações: {pedido.get('observacoes', 'Nenhuma')}")
    print(f"📌 Status: {pedido.get('status', 'Sem status')}")
    print("-" * 40)

    pedido_foi_editado = False

    if obter_texto("\n✏️  Deseja editar os itens do pedido? (s/n): ").lower() == 's':
        itens_atualizados = []
        
        print("\n🛒 Adicione novos itens ao pedido (digite 'sair' para finalizar):")
        while True:
            item = obter_texto("➕ Novo item: ")
            if item.lower() == "sair":
                break
            itens_atualizados.append(item)
    
        if itens_atualizados:
            pedido['itens'] = itens_atualizados
            print("✅ Itens atualizados com sucesso!")
            pedido_foi_editado = True
        else:
            print("⚠️ Nenhum item novo foi adicionado.")

    if obter_texto("\n🗒️  Deseja editar a observação do pedido? (S/N): ").lower() == 's':
        observacao = obter_texto("\n🗒️  Escreva a nova observação do pedido: ")
        if observacao == '':
            observacao = 'Nenhuma'
        pedido["observacoes"] = observacao
        print("✅ Observação atualizada com sucesso!")
        pedido_foi_editado = True
        
    if pedido_foi_editado:
        salvar_pedidos(pedidos)
        print(f"\n🎉 Pedido da mesa {mesa_selecionada} atualizado com sucesso!\n")
    else:
        print("\nℹ️ Nenhuma alteração foi feita no pedido.")
    
    retorno_main()

def remover_pedido(pedidos: dict):
    limpar_console()
    print("========== ❌ REMOVER PEDIDO ❌ ==========\n")

    obter_mesa = obter_int("🔢 Digite o número da mesa: ", '⚠️ O número da mesa não pode ser negativo. Tente novamente.')

    for pedido in pedidos["pedidos"]:
        if pedido["mesa"] == obter_mesa:
            print("\n✅ Mesa encontrada!")
            print("-" * 40)
            print(f"🍽️  Itens: {', '.join(pedido['itens']) if pedido['itens'] else 'Nenhum item'}")
            print(f"📝 Observações: {pedido.get('observacoes', 'Nenhuma')}")
            print(f"📌 Status: {pedido['status'] if pedido['status'] else 'Sem status'}")
            print("-" * 40)

            cancelar_pedido = obter_texto("\n❓ Deseja mesmo cancelar o pedido? (s/n): ").lower()
            if cancelar_pedido == "s":
                pedidos["pedidos"].remove(pedido)
                salvar_pedidos(pedidos)
                print(f"\n✅ Pedido da mesa {obter_mesa} removido com sucesso!")
            else:
                print("\nℹ️  O pedido não foi cancelado.")
            break
    else:
        print(f"\n⚠️  Nenhum pedido encontrado para a mesa {obter_mesa}.")

    retorno_main()
