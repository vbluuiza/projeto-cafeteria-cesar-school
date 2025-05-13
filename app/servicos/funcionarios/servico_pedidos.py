import json

from app.repositorios.repositorio_pedidos import carregar_pedidos, salvar_pedidos
from app.servicos.utilitarios_servicos.utils import exibir_cardapio
from app.utils.utilitarios_global import limpar_console
from app.utils.utilitarios_global import obter_texto, obter_int
from app.utils.utilitarios_global import STATUS_PEDIDO


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
        observacao = obter_texto('Gostaria de adicionar alguma observacao?: ')
        if observacao == '':
            observacao = 'Nenhuma'

        pedido = {
            'mesa': mesa_em_atendimento,
            'itens': itens_pedidos,
            'observacoes': observacao,
            'status': STATUS_PEDIDO[0]
        }

        pedidos['pedidos'].append(pedido)
        salvar_pedidos(pedidos)

        break

def editar_pedido(cardapio, pedidos, mesas):
    limpar_console()
    exibir_cardapio()

    print ("========== ☕ EDITAR PEDIDO ☕ ==========")

    pedidos_dados = pedidos['mesas']
    mesas_com_pedidos = [pedido["mesa"] for pedido in pedidos_dados]
    
    if not mesas_com_pedidos:
        limpar_console()
        print("❌ Não há mesas com pedidos ativos no momento.")
        return
    
    print("\n📋 Mesas com pedidos ativos:")
    for mesa in mesas_com_pedidos:
        print(f"   ➤   Mesa {mesa}")
    
    while True:
        mesa_selecionada = obter_int("\n🔢 Informe o número da mesa selecionada: ")
        if mesa_selecionada in mesas_com_pedidos:
            break
        else:
            print("⚠️ Mesa não encontrada com pedido ativo.")
        
    
    pedido = next((pedido for pedido in pedidos_dados if pedido["mesa"] == mesa_selecionada), None)

    print(f"\n📦 Pedido atual da mesa {mesa_selecionada}:")
    print("-" * 40)
    print(f"🍽️  Itens: {', '.join(pedido['itens'])}")
    print(f"📝 Observações: {pedido.get('observacoes', 'Nenhuma')}")
    print(f"📌 Status: {pedido['status']}")
    print("-" * 40)

    pedido_foi_editado = False

    if obter_texto("\n✏️ Deseja editar os itens do pedido? (s/n): ").lower() == 's':
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

        if obter_texto("\n🗒️ Deseja editar a observação do pedido? (S/N): ").lower() == 's':
            nova_observacao = obter_texto("💬 Digite a nova observação: ")
        if nova_observacao == '':
            nova_observacao = 'Nenhuma'
        pedido["observacoes"] = nova_observacao
        print("✅ Observação atualizada com sucesso!")
        pedido_foi_editado = True
        

    if pedido_foi_editado:
        salvar_pedidos(pedidos)
        print(f"\n🎉 Pedido da mesa {mesa_selecionada} atualizado com sucesso!\n")
    else:
        print("\nℹ️ Nenhuma alteração foi feita no pedido.")

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