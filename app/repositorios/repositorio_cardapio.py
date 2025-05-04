import json
from app.utilitarios.utils import limpar_console

def carregar_cardapio():
    try:
        with open('app/dados/dados_json/cardapio.json', 'r', encoding='utf-8') as file:
            return json.load(file)
    except FileNotFoundError:
        print('Erro: Arquivo não encontrado.')
        return None
    except json.JSONDecodeError:
        print('❌ Erro ao ler o JSON do cardápio.')
        return
    
cardapio = carregar_cardapio()

def exibir_cardapio():
    limpar_console()
    print('\n' + '☕🍹CARDÁPIO DE BEBIDAS ☕🍹'.center(56, '─'))
    print('─' * 60)
    exibir_bebidas()
    
    print('\n' + '🍨🥪 CARDÁPIO DE LANCHES E SOBREMESAS 🍨🥪 '.center(56, '─'))
    print('─' * 60)
    exibir_lanches()

def exibir_bebidas():
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
            
def exibir_lanches():
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
    
from app.utilitarios.utils import obter_float, obter_int, obter_texto

def gerar_proximo_id(cardapio: dict) -> int:
    return max(
        (item['id'] for categoria in cardapio.values()
                        for subcategoria in categoria.values()
                            for item in subcategoria),
        default=0
    ) + 1

def cadastrar_item():
    limpar_console()
    print('\n🌟 📝 Cadastro de Novo Item no Cardápio 🌟')
    print('-' * 50)
    
    categorias_validas = {
        'bebidas': ['cafes', 'cafes_especiais', 'outras_bebidas'],
        'lanches': ['sanduiches', 'sobremesas']
    }

    carregar_cardapio()
    
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
    
    try:
        with open('app/dados/dados_json/cardapio.json', 'w', encoding='utf-8') as file:
            json.dump(cardapio, file, ensure_ascii=False, indent=4)
            print("\n✅ Cardápio atualizado e salvo com sucesso!")
    except Exception as e:
        print(f'\n⚠️ Erro ao salvar o cardápio: {e}')    