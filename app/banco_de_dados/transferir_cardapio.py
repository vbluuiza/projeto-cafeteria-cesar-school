from conexao import conectar
import json

CAMINHO = 'app/banco_de_dados/dados_json/cardapio.json'


def carregar_cardapio():
    try:
        with open(CAMINHO, 'r', encoding='utf-8') as file:
            return json.load(file)
    except FileNotFoundError:
        print('Erro: Arquivo não encontrado.')
    except json.JSONDecodeError:
        print('❌ Erro ao ler o JSON do cardápio.')

    return {}    

cardapio = carregar_cardapio()

def transferir_dados_json_para_sqlite(cardapio:dict):
    itens = []
    for item in cardapio:
        
        nome = item['nome']
        descricao = item['descricao']
        ingredientes = item['ingredientes']
        preco = item['preco']
        subcategoria = item['subcategoria']
        categoria = item['categoria']
        
        itens.append((nome, descricao, ingredientes, preco, subcategoria, categoria))
        
    conexao = conectar()
    cursor = conexao.cursor()

    for item in itens:
        cursor.execute('''
            INSERT INTO cardapio (nome, descricao, ingredientes, preco, subcategoria, categoria)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', item)
    
    conexao.commit()
    conexao.close()
    
    print(f'Itens inseridos no cardápio')
    
transferir_dados_json_para_sqlite(cardapio)