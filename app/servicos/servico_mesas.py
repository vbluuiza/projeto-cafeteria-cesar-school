import json
from app.repositorios.repositorio_mesas import carregar_mesas, salvar_mesas
from app.utilitarios.utils import limpar_console
from app.utilitarios.utils import obter_int


def cadastrar_mesa():

    dados_das_mesas = carregar_mesas()

    lista_de_mesas = dados_das_mesas['lista_de_mesas']
    total_de_mesas = dados_das_mesas['total_de_mesas']

    limpar_console()
    print('\n🌟 📝 Cadastro de nova mesa 🌟')
    print('-' * 50)
    quantia_de_mesas_a_adicionar = obter_int('Quantas mesas serão adicionadas: ')
    
    for i in range(quantia_de_mesas_a_adicionar):
        
        new_id = total_de_mesas+1
        nova_mesa = {
            'id': new_id,
            'status': 0
        } 
        lista_de_mesas.append(nova_mesa)
        total_de_mesas += 1
        salvar_mesas(dados_das_mesas)
    
    print(f'\n✅ "{quantia_de_mesas_a_adicionar} Mesas foram adicionadas com sucesso!')

def remover_mesa():

    dados_das_mesas = carregar_mesas()

    limpar_console()
    print('\n🌟 📝 REMOVER MESAS 🌟')
    print('-' * 50)
    quantia_de_mesas_a_remover = obter_int('Quantas mesas serão removidas: ')
    
    for i in range(quantia_de_mesas_a_remover):
        dados_das_mesas['lista_de_mesas'].pop()
        dados_das_mesas['total_de_mesas'] -=1

    salvar_mesas(dados_das_mesas)
    
    print(f'\n✅ "{quantia_de_mesas_a_remover} Mesas foram removidas com sucesso!')
