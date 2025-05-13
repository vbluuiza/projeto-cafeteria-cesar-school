import json

CAMINHO = 'app/dados_json/mesas.json'

def carregar_mesas():
    try:
        with open(CAMINHO, 'r', encoding='utf-8') as file:
            return json.load(file)
    except FileNotFoundError:
        print('Erro: Arquivo não encontrado.')
    except json.JSONDecodeError:
        print('❌ Erro ao ler o JSON das mesas.')

    return {}    


def salvar_mesas(mesas):
    try:
        with open(CAMINHO, 'w', encoding='utf-8') as file:
            json.dump(mesas, file, ensure_ascii=False, indent=4)
    except FileNotFoundError:
        print('Erro: Arquivo não encontrado.')
    except json.JSONDecodeError:
        print('❌ Erro ao ler o JSON das mesas.')

    return {}    
