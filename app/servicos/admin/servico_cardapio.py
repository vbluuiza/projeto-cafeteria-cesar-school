import json

from app.repositorios.repositorio_cardapio import carregar_cardapio, salvar_cardapio

from app.utils.utilitarios_global import limpar_console
from app.utils.utilitarios_global import obter_float, obter_texto

from app.utils.utilitarios_cardapio import gerar_proximo_id, obter_categoria_e_subcategoria_valida

def cadastrar_item(cardapio:dict):
    limpar_console()
    
    print('\n🌟 📝 CADASTRO DE NOVO ITEM NO CARDÁPIO 🌟')
    print('-' * 50)

    categoria_geral, categoria_especifica = obter_categoria_e_subcategoria_valida()

    _id = gerar_proximo_id(cardapio)
    nome = obter_texto('📛 Nome do item: ')
    descricao = obter_texto('🖋️  Descrição do item: ')
    ingredientes_str = obter_texto('🥄 Ingredientes (separados por vírgula): ')
    preco = obter_float('💲 Preço (ex: 12.50): ')
    ingredientes = [ingrediente.strip() for ingrediente in ingredientes_str.split(',')]
    categoria_item = obter_texto('🖋️  Categoria do item: ')
    
    novo_item = {
        'id': _id,
        'nome': nome,
        'descricao': descricao,
        'ingredientes': ingredientes,
        'preco': preco,
        'categoria': categoria_item
    }
    
    
    cardapio[categoria_geral][categoria_especifica].append(novo_item)
    print(f'\n✅ "{nome.title()}" foi adicionado à categoria "{categoria_especifica}" dentro de "{categoria_geral}" com sucesso!')
    
    salvar_cardapio(cardapio)
        
def remover_item_cardapio(cardapio:dict):
    limpar_console()
    
    print('\n' + '🚮🗑️ REMOVER ITEM CARDÁPIO  🗑️🚮'.center(46, '─'))
    print('-' * 50)
    
    categoria_geral, categoria_especifica = obter_categoria_e_subcategoria_valida()
    
    item_remover = obter_texto('\n✏️  Informe o nome exato do item que deseja remover: ')
    item_encontrado = False

    for item in cardapio[categoria_geral][categoria_especifica]:
        if item['nome'] == item_remover:
            item_encontrado = True
            cardapio[categoria_geral][categoria_especifica].remove(item)
            print(f'\n✅ Item "{item_remover}" removido com sucesso!')
            salvar_cardapio(cardapio)
            break  

    if not item_encontrado:
        print('\n❌ Item não encontrado. Verifique o nome e tente novamente.')

def editar_item_cardapio(cardapio:dict):
    limpar_console()
    
    print('\n' + '🌟📝 EDITAR ITEM NO CARDÁPIO 📝🌟'.center(46, '─'))
    print('-' * 50)
    
    categoria_geral, categoria_especifica = obter_categoria_e_subcategoria_valida()
    
    categoria_especifica_items = [item['nome'] for item in cardapio[categoria_geral][categoria_especifica]]    
    print(f'\n📋 Itens disponíveis em "{categoria_especifica}" ({categoria_geral}):\n')
    for item in categoria_especifica_items:
        print(f'  ➤  {item}')

    item_editar = obter_texto('\n✏️  Informe o nome exato do item que deseja editar: ')
    item_encontrado = False

    for item in cardapio[categoria_geral][categoria_especifica]:
        if item['nome'] == item_editar:
            item_encontrado = True
            print('\n🔧 Preencha os novos dados do item:\n')
            
            id_original = item['id']
            categoria_original = item['categoria']

            item['nome'] = obter_texto(f'📛 Novo nome do item: ')
            item['descricao'] = obter_texto(f'🖋️  Nova descrição do item: ')
            ingredientes_str = obter_texto('🥄 Ingredientes (separados por vírgula): ')
            ingredientes = [ingrediente.strip() for ingrediente in ingredientes_str.split(',')]
            item['ingredientes'] = ingredientes
            item['preco'] = obter_float(f'💰 Preco Antigo {item['preco']} | Novo preço (ex: 12.50) : ')

            item['id'] = id_original
            item['categoria'] = categoria_original
            
            salvar_cardapio(cardapio)
            print('\n✅ Item editado com sucesso!')
            break
        
    if not item_encontrado:
        print('\n❌ Item não encontrado. Verifique o nome e tente novamente.')
           
def buscar_item_cardapio(cardapio:dict):
    limpar_console()
    
    print('\n🔍 📋 BUSCAR ITEM DO CARDÁPIO 📋 🔍')
    print('-' * 50)

    item_cardapio_nome = obter_texto("🔢 Informe o nome do item do cardápio que deseja buscar: ")
    item = next((item for categoria in cardapio.values() for subcategoria in categoria.values() for item in subcategoria if item['nome'] == item_cardapio_nome), None)
    
    if item:
        print(f"\n✅ Item encontrado!\n")
        print(f"🪑 ID do Item: {item['id']}")
        print(f'📌 Nome do Item: {item['nome']} ')
        print(f'🖋️  Descrição do item: {item['descricao']} ')
        print(f'🥄 Ingredientes do item: {item['ingredientes']} ')
        print(f'💲 Preço do item: R${item['preco']} ')
        print(f'🖋️  Categoria do item: {item['categoria']} ')
    else:
        print(f'\n❌ Item não encontrado. Verifique o nome e tente novamente.')