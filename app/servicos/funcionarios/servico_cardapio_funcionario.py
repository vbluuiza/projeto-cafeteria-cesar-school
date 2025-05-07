import json
from app.repositorios.repositorio_cardapio import carregar_cardapio
from app.utils.utilitarios_global import limpar_console
from app.utils.utilitarios_global import obter_int, obter_texto

def buscar_item_cardapio():
    cardapio = carregar_cardapio()
    
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