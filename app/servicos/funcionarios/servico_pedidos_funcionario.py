import json
from app.repositorios.repositorio_pedidos import carregar_dados
from app.utils.utilitarios_global import limpar_console
from app.utils.utilitarios_global import obter_texto
from app.servicos.utilitarios_servicos.utils import exibir_cardapio
from app.repositorios.repositorio_cardapio import carregar_cardapio

def criar_pedido(cardapio:dict):
    limpar_console()
    exibir_cardapio()

    pedidos_dados = carregar_dados()
    mesa = 1
    total_mesas = pedidos_dados["total_mesas"] - mesa

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

