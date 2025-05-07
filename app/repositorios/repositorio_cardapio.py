import json

CAMINHO = 'app/dados/dados_json/cardapio.json'

def carregar_cardapio():
    try:
        with open(CAMINHO, 'r', encoding='utf-8') as file:
            return json.load(file)
    except FileNotFoundError:
        print('Erro: Arquivo não encontrado.')
    except json.JSONDecodeError:
        print('❌ Erro ao ler o JSON do cardápio.')

    return {}    


def salvar_cardapio(cardapio):
    try:
        with open(CAMINHO, 'w', encoding='utf-8') as file:
            json.dump(cardapio, file, ensure_ascii=False, indent=4)
    except FileNotFoundError:
        print('Erro: Arquivo não encontrado.')
    except json.JSONDecodeError:
        print('❌ Erro ao ler o JSON do cardápio.')

    return {}    