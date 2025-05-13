import json
from app.repositorios.repositorio_mesas import salvar_mesas
from app.utils.utilitarios_global import limpar_console
from app.utils.utilitarios_global import obter_int
from app.servicos.utilitarios_servicos.utils import STATUS_MESA



def cadastrar_mesa(mesas:dict):
    
    limpar_console()
    print('\n🌟 📝 Cadastro de nova mesa 🌟')
    print('-' * 50)
    quantia_de_mesas_a_adicionar = obter_int('Quantas mesas serão adicionadas: ')
    
    for i in range(quantia_de_mesas_a_adicionar):
        
        new_id = mesas['total_de_mesas']+1
        nova_mesa = {
            'id': new_id,
            'status': STATUS_MESA[0]
        } 
        mesas['lista_de_mesas'].append(nova_mesa)
        mesas['total_de_mesas'] += 1
        
    salvar_mesas(mesas)
    
    if(quantia_de_mesas_a_adicionar == 1):
        print(f'\n✅ "{quantia_de_mesas_a_adicionar} Mesa foi adicionada com sucesso!')
    else:
        print(f'\n✅ "{quantia_de_mesas_a_adicionar} Mesas foram adicionadas com sucesso!')

def remover_mesa(mesas:dict):

    limpar_console()
    print('\n🌟 📝 REMOVER MESAS 🌟')
    print('-' * 50)
    quantia_de_mesas_a_remover = obter_int('Quantas mesas serão removidas: ')
    
    for i in range(quantia_de_mesas_a_remover):
        mesas['lista_de_mesas'].pop()
        mesas['total_de_mesas'] -=1

    salvar_mesas(mesas)
    
    if(quantia_de_mesas_a_remover == 1):
        print(f'\n✅ "{quantia_de_mesas_a_remover} Mesa foi removida com sucesso!')
    else:
        print(f'\n✅ "{quantia_de_mesas_a_remover} Mesas foram removidas com sucesso!')

def buscar_mesa_id(mesas:dict):
    
    limpar_console()
    print('\n🔍 📋 BUSCAR MESA POR ID 📋 🔍')
    print('-' * 50)

    buscar_mesa = obter_int("🔢 Informe o ID da mesa que deseja buscar: ")
    for mesa in mesas['lista_de_mesas']:
        if mesa['id'] ==  buscar_mesa:
            print(f"\n✅ Mesa encontrada!")
            print(f"🪑 ID da Mesa: {mesa['id']}")
            print(f'📌 Status: {mesa['status']} ')
            break
    else:
        print(f'\n❌ Mesa não encontrada. Verifique o ID e tente novamente.')

def listar_mesas(mesas:dict):
    
    limpar_console()
    print('\n🌟 📝 LISTANDO MESAS 🌟')
    print('-' * 50)
    
    for mesa in mesas['lista_de_mesas']:
        print(f"🪑 ID da Mesa: {mesa['id']}")
        print(f'📌 Status: {mesa['status']} ')
        print('-' * 50)