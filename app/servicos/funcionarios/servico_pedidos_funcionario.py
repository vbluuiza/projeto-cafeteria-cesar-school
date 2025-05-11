import json

from app.repositorios.repositorio_pedidos import carregar_pedidos, salvar_pedidos
from app.repositorios.repositorio_cardapio import carregar_cardapio

from app.servicos.cliente.servico_cardapio_cliente import exibir_cardapio

from app.utils.utilitarios_global import limpar_console
from app.utils.utilitarios_global import obter_texto, obter_int
from app.utils.utilitarios_global import STATUS_PEDIDO

def criar_pedido(cardapio: dict, pedidos: dict, mesas: dict):
    limpar_console()

    total_de_mesas = mesas['total_de_mesas']
    mesa_em_atendimento = obter_int("Mesa atendida: ")

    if mesa_em_atendimento > total_de_mesas:
        print(f"❌ Mesa inexistente. Mesas disponíveis: 1 até {total_de_mesas}")
        return

    exibir_cardapio()
    print("========== ☕ PEDIDO NOVO ☕ ==========")
    print("\n📌 Favor, escolha os itens que desejar!")

    itens_cardapio = [
        {'nome': item['nome'], 'preco': item['preco']}
        for categoria in cardapio.values()
        for subcategoria in categoria.values()
        for item in subcategoria
    ]

    itens_pedidos = []

    while True:
        pedido = obter_texto("\n🍽️  O que gostaria de pedir: ")

        item_encontrado = next((item for item in itens_cardapio if item['nome'] == pedido), None)

        if item_encontrado:
            itens_pedidos.append(item_encontrado)
            print(f"\n✅ '{item_encontrado['nome']}' adicionado com sucesso!")
        else:
            print(f"\n❌ Item '{pedido}' não encontrado no cardápio.")
            continue

        adicionar_item = obter_texto("\n➕ Gostaria de pedir mais alguma coisa? (S/N): ").lower()
        if adicionar_item == 'n':
            break

    if not itens_pedidos:
        print("\n⚠️ Nenhum item válido foi adicionado. Pedido cancelado.")
        return

    observacao = obter_texto('\n🗒️  Gostaria de adicionar alguma observação?: ')
    if observacao == '':
        observacao = 'Nenhuma'

    novo_pedido = {
        'mesa': mesa_em_atendimento,
        'itens': itens_pedidos,
        'observacoes': observacao,
        'status': STATUS_PEDIDO[0]
    }

    pedidos['pedidos'].append(novo_pedido)
    salvar_pedidos(pedidos)

    print("\n🎉 Pedido realizado com sucesso!")
    print(f"📍 Mesa: {mesa_em_atendimento}")
    print("🧾 Itens pedidos:")
    for item in itens_pedidos:
        print(f" ➤   {item['nome']}   |     ➤  R${item['preco']:.2f}")
    print(f"💬 Observações: {observacao}")
    print(f"📦 Status inicial: {STATUS_PEDIDO[0]}")


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

def remover_pedido(pedidos: dict):
    limpar_console()
    print("========== ❌ REMOVER PEDIDO ❌ ==========\n")

    obter_mesa = obter_int("🔢 Digite o número da mesa: ")

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