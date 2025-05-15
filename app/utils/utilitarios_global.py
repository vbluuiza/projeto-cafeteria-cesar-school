import json
import os
def limpar_console():
    os.system('cls' if os.name == 'nt' else 'clear')
    
def obter_texto(msg):
    return input(msg).strip()

def obter_int(msg):
     while True:
        try:
            valor = int(input(msg).strip())
            if valor > 0:
                return valor
            else:
                print("⚠️ O preço não pode ser negativo.")
        except ValueError:
            print("⚠️ Por favor, digite um número inteiro válido.")

def obter_float(msg):
    while True:
        try:
            valor = float(input(msg).strip())
            if valor > 0:
                return valor
            else:
                print("⚠️ O preço não pode ser negativo.")
        except ValueError:
            print("⚠️ Por favor, digite um número válido para o preço.")


STATUS_PEDIDO = {
    0: 'Pedido Aprovado',
    1: 'Em preparo',
    2: 'Pronto',
    3: 'Entregue',
    4: 'Cancelado'
}

def retorno_main():
    from main import inicializar_cafeteria
    print("\n" + "=" * 50)
    print('1️⃣  Retonar')
    print('0️⃣  Finalizar')
    print("=" * 50)

    while True:
        try:
            opcao = int(input('👉 Escolha uma opção: '))
            if opcao in (0, 1):
                break
            else:
                print('❌ Opção inválida! Digite um número entre (0, 1)')
        except ValueError:
                print('❌ Opção inválida! Digite um número.')

    if opcao == 1:
            inicializar_cafeteria()

    elif opcao == 0:
        print('\n👋 Até logo!\n')

def retornar_para_menu():
    from main import inicializar_cafeteria

    inicializar_cafeteria()
    
from app.repositorios.repositorio_cardapio import carregar_cardapio
from app.utils.utilitarios_global import limpar_console, obter_texto

def gerar_proximo_id(cardapio: dict) -> int:
    return max(
        (item['id'] for categoria in cardapio.values()
                        for subcategoria in categoria.values()
                            for item in subcategoria),
        default=0
    ) + 1
    
def obter_categoria_e_subcategoria_valida():
    categorias_validas = {
        'bebidas': ['cafes', 'cafes_especiais', 'outras_bebidas'],
        'lanches': ['sanduiches', 'sobremesas']
    }
    
    categoria_geral = obter_texto('\n📂 Digite a Categoria Geral (ex: bebidas, lanches): ').lower()
    if categoria_geral not in categorias_validas:
        print('\n⚠️ Categoria geral inválida! Verifique e tente novamente. ')
        return
        
        
    categoria_especifica = obter_texto("🏷️  Digite a Categoria Específica (ex: cafes, cafes_especiais, sobremesas...): ").lower()
    if categoria_especifica not in categorias_validas[categoria_geral]:
        print('\n⚠️ Categoria específica inválida! Verifique e tente novamente.')
        return
    
    return categoria_geral, categoria_especifica    

def exibir_titulo_cardapio(emoji, categoria_formatada):
    print(f"\n{emoji} {categoria_formatada.upper()} {emoji}".ljust(45) + f"Preço".rjust(10))
    print(' ' + '-' * 58)

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
            
            exibir_titulo_cardapio(emoji, categoria_formatada)
            
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
            
            exibir_titulo_cardapio(emoji, categoria_formatada)
            
            for opcao_lanche in lanches:
                nome = opcao_lanche['nome']
                preco = f'R$ {opcao_lanche['preco']:.2f}'
                print(f'  ➤ {nome.ljust(40, '.')} {preco.rjust(12)}')
    print('\n' + '─' * 60 + '\n')

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


STATUS_MESA = {
    0: 'Disponível',
    1: 'Ocupada',
    3: 'Em espera',
}
