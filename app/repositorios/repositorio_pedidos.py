import json

CAMINHO = 'app/dados/dados_json/pedidos.json'

def carregar_dados():
    try:
        with open(CAMINHO, 'r', encoding='utf-8') as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        print('❌ Erro ao ler o JSON do cardápio.')    
    return {}

def  salvar_dados(dados):
    try:
        with open(CAMINHO, 'w', encoding='utf-8') as file:
            json.dump(dados, file, ensure_ascii=False, indent=4)
    except (FileNotFoundError, json.JSONDecodeError):
        print('❌ Erro ao ler o JSON do cardápio.')
        
    return {}