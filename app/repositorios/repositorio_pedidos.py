import json

def carregar_dados():
    try:
        with open('dados.json', 'r') as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        print('❌ Erro ao ler o JSON do cardápio.')    
    return {'mesas': {}, 'pedidos': {}}

def  salvar_dados(dados):
    try:
        with open('dados.json', 'w') as file:
            json.dump(dados, file, indent=4)
    except (FileNotFoundError, json.JSONDecodeError):
        print('❌ Erro ao ler o JSON do cardápio.')
        
    return{}