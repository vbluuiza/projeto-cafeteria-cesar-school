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
