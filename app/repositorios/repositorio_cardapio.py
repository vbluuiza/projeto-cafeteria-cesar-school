import json

def carregar_cardapio():
    try:
        with open('app/dados/dados_json/cardapio.json', 'r', encoding='utf-8') as file:
            return json.load(file)
    except FileNotFoundError:
        print('Erro: Arquivo não encontrado.')
    except json.JSONDecodeError:
        print('❌ Erro ao ler o JSON do cardápio.')

    return {}    

