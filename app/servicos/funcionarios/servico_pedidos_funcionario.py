import json
from app.repositorios.repositorio_pedidos import carregar_pedidos, salvar_pedidos
from app.utils.utilitarios_global import limpar_console
from app.utils.utilitarios_global import obter_texto, obter_int
from app.servicos.cliente.servico_cardapio_cliente import exibir_cardapio
from app.repositorios.repositorio_cardapio import carregar_cardapio

def criar_pedido(cardapio:dict, pedidos:dict, mesas:dict):
    limpar_console()

    total_de_mesas = mesas['total_de_mesas']

    mesa_em_atendimento = obter_int("Mesa atendida: ")
    
    if mesa_em_atendimento > total_de_mesas:
        print(f"Mesa inexistente, mesas disponiveis: 1 até {total_de_mesas}")

    exibir_cardapio()

    print("========== ☕ PEDIDO NOVO ☕ ==========")
    print("\nFavor, escolha os itens que desejar!")

    itens_cardapio_nome = [item['nome'] for categoria in cardapio.values() for subcategoria in categoria.values() for item in subcategoria]
    
    itens_pedidos = []
    while True:
        
        pedido = obter_texto("\nO que gostaria de pedir: ")

        if pedido not in itens_cardapio_nome:
            print("\nItem não encontrado.")
            continue
        
        itens_pedidos.append(pedido)
        print("\nItem adicionado com sucesso!")

        adicionar_item = obter_texto("\nGostaria de pedir mais alguma coisa? (s/n): ").lower()
        
        if adicionar_item != 'n':
            continue
        
        break

def editar_pedido(cardapio, pedidos, mesas):
    limpar_console()
    exibir_cardapio()
    pedidos_dados = carregar_pedidos()
    pedidos = pedidos_dados.get("pedidos", [])

    print ("========== ☕ EDITAR PEDIDO ☕ ==========")

    mesas_com_pedidos = [pedido["mesa"] for pedido in pedidos]
    if not mesas_com_pedidos:
        limpar_console()
        print("❌ Não há mesas com pedidos ativos no momento.")
        return
    
    print("\nMesas com pedidos ativos:")
    for mesa in mesas_com_pedidos:
        print(f"- Mesa {mesa}")
    
    while True:
        try:
            mesa_selecionada = int (input("\nInforme o número da mesa selecionada:")).strip()
            if mesa_selecionada in mesas_com_pedidos:
                break
            else:
                print("⚠️ Mesa não encontrada com pedido ativo.")
        except ValueError:
            print("❌ Digite um número válido para a mesa.")
    
    pedido = next((p for p in pedidos_dados if p["mesa"] == mesa_selecionada), None)

    print(f"\nPedido atual da mesa {mesa_selecionada}:")
    print(f"- Itens: {pedido['itens']}")
    print(f"- Observações: {pedido.get('observacoes', 'Nenhuma')}")
    print(f"- Status: {pedido['status']}")

    editar_itens = input("\nDeseja editar os itens do pedido? (s/n): ").lower()
    if editar_itens == 's':
        novos_itens = []
        while True:
            item = input("\nDigite o nome de um novo item ou digite 'Sair'").lower
            if item == "sair":
                break
            else:
                novos_itens.append(item)
                if novos_itens:
                    pedido['itens'] = novos_itens
                    print("\n✅Itens atualizados com sucesso.")
                else:
                    print("\n⚠️Nenhum item novo foi adicionado.")

    while True:
        nova_obs = input("\nDigite nova observação ou digite 'sair': ")
        if nova_obs == "sair":
            break
        else:
            pedido["observacoes"] = nova_obs
            print ("Observação adicionada com sucesso!")

    novo_status = obter_texto("Digite o novo status (em preparo / pronto / entregue): ").lower()
    if novo_status in ['em preparo', 'pronto', 'entregue']:
        pedido["status"] = novo_status
    else:
        print("⚠️ Status inválido. Status anterior mantido.")

    salvar_pedidos(pedidos_dados)
    print("\n✅ Pedido atualizado com sucesso!")