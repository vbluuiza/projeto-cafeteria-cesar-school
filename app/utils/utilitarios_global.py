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