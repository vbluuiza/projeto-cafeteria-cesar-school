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