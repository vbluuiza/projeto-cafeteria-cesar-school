import json

CAMINHO = 'app/dados_json/pedidos.json'

def carregar_pedidos():
    try:
        with open(CAMINHO, 'r', encoding='utf-8') as file:
            return json.load(file)
    except FileNotFoundError:
        print('Erro: Arquivo não encontrado.')    
    except json.JSONDecodeError:
        print('❌ Erro ao ler o JSON do cardápio.')    

    return {}

def  salvar_pedidos(pedidos):
    try:
        with open(CAMINHO, 'w', encoding='utf-8') as file:
            json.dump(pedidos, file, ensure_ascii=False, indent=4)
    except (FileNotFoundError, json.JSONDecodeError):
        print('❌ Erro ao ler o JSON do cardápio.')
        
    return {}
