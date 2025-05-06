import json
from app.repositorios.repositorio_cardapio import carregar_cardapio, salvar_cardapio
from app.utilitarios.utils import limpar_console
from app.utilitarios.utils import obter_float, obter_int, obter_texto
from app.utilitarios.utils import gerar_proximo_id

def exibir_cardapio():
    limpar_console()
    
    cardapio = carregar_cardapio()
    if cardapio:
        print('\n' + '☕🍹CARDÁPIO DE BEBIDAS ☕🍹'.center(56, '─'))
        print('─' * 60)
        exibir_bebidas(cardapio)
        
        print('\n' + '🍨🥪 CARDÁPIO DE LANCHES E SOBREMESAS 🍨🥪 '.center(56, '─'))
        print('─' * 60)
        exibir_lanches(cardapio)
        
    else:
        print('❌ Não foi possível exibir o cardápio.')
        return None

def exibir_bebidas(cardapio: dict):
    for categoria, bebidas in cardapio['bebidas'].items():
        if bebidas:
            categoria_formatada = categoria.replace('_', ' ').title()
            emoji = '☕' if 'cafe' in categoria.lower() else '🍹'
            print(f"\n{emoji} {categoria_formatada.upper()} {emoji}".center(60, ' '))
            print(' ' + '-' * 58)
            for opcao_bebida in bebidas:
                nome = opcao_bebida['nome']
                preco = f'R$ {opcao_bebida['preco']:.2f}'
                print(f'  ➤ {nome.ljust(40, '.')} {preco.rjust(12)}')
    print('\n' + '─' * 60 + '\n')
            
def exibir_lanches(cardapio: dict):
    for categoria, lanches in cardapio['lanches'].items():
        if lanches:
            categoria_formatada = categoria.replace('_', ' ').title()
            emoji = '🥪' if 'sanduiches' in categoria.lower() else '🍨'
            print(f"\n{emoji} {categoria_formatada.upper()} {emoji}".center(60, ' '))
            print(' ' + '-' * 58)
            for opcao_lanche in lanches:
                nome = opcao_lanche['nome']
                preco = f'R$ {opcao_lanche['preco']:.2f}'
                print(f'  ➤ {nome.ljust(40, '.')} {preco.rjust(12)}')
    print('\n' + '─' * 60 + '\n')

def cadastrar_item(cardapio:dict):
    limpar_console()
    print('\n🌟 📝 Cadastro de Novo Item no Cardápio 🌟')
    print('-' * 50)
    
    categorias_validas = {
        'bebidas': ['cafes', 'cafes_especiais', 'outras_bebidas'],
        'lanches': ['sanduiches', 'sobremesas']
    }

    categoria_geral = obter_texto('\n📂 Digite a Categoria Geral (ex: bebidas, lanches): ').lower()
    if categoria_geral not in categorias_validas:
        print('\n⚠️ Categoria geral inválida!')
        return
        
        
    categoria_especifica = obter_texto("🏷️  Digite a Categoria Específica (ex: cafes, cafes_especiais, sobremesas...): ").lower()
    if categoria_especifica not in categorias_validas[categoria_geral]:
        print('\n⚠️ Categoria específica inválida!')
        return
    
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
        
        
def editar_item(cardapio:dict):
    limpar_console()
    print('\n' + '🌟📝 EDITAR ITEM NO CARDÁPIO 📝🌟'.center(46, '─'))
    print('-' * 50)
    
    categoria_editar = obter_texto('\n📂 Informe a categoria geral do item (ex: bebidas, lanches): ').lower()
    if categoria_editar not in cardapio:
        print('\n❌ Categoria não encontrada. Verifique e tente novamente.')
        return
    
    categoria_especifica_editar = obter_texto('\n📁 Informe a subcategoria do item (ex: cafés, sobremesas): ').lower()
    if categoria_especifica_editar not in cardapio[categoria_editar]:
        print('\n❌ Subcategoria não encontrada. Verifique e tente novamente.')
        return
    
    categoria_especifica_items = [item['nome'] for item in cardapio[categoria_editar][categoria_especifica_editar]]    
    print(f'\n📋 Itens disponíveis em "{categoria_especifica_editar}" ({categoria_editar}):\n')
    for item in categoria_especifica_items:
        print(f'  ➤  {item}')

    item_editar = obter_texto('\n✏️  Informe o nome exato do item que deseja editar: ')
    item_encontrado = False

    for item in cardapio[categoria_editar][categoria_especifica_editar]:
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
        
        