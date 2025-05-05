def obter_texto(msg):
    return input(msg).strip()

def obter_int(msg):
     while True:
        try:
            return int(input(msg).strip())
        except ValueError:
            print("⚠️ Por favor, digite um número inteiro válido.")

def obter_float(msg):
    while True:
        try:
            valor = float(input(msg).strip())
            if valor >= 0:
                return valor
            else:
                print("⚠️ O preço não pode ser negativo.")
        except ValueError:
            print("⚠️ Por favor, digite um número válido para o preço.")
            
import os
def limpar_console():
    os.system('cls' if os.name == 'nt' else 'clear')
    
def gerar_proximo_id(cardapio: dict) -> int:
    return max(
        (item['id'] for categoria in cardapio.values()
                        for subcategoria in categoria.values()
                            for item in subcategoria),
        default=0
    ) + 1
