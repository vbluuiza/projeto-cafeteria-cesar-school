import json

from app.repositorios.repositorio_mesas import salvar_mesas

from app.utils.utilitarios_global import limpar_console, retorno_main, obter_int, obter_texto, STATUS_MESA

def cadastrar_mesa(mesas:dict):
    limpar_console()
    
    print('\n🌟 📝 Cadastro de nova mesa 🌟')
    print('-' * 50)
    
    quantia_de_mesas_a_adicionar = obter_int('🔢 Quantas mesas serão adicionadas: ', '⚠️ A quantidade de mesas não pode ser negativa. Tente novamente\n')
    
    for i in range(quantia_de_mesas_a_adicionar):
        
        new_id = mesas['total_de_mesas']+1
        nova_mesa = {
            'id': new_id,
            'status': STATUS_MESA[0]
        } 
        mesas['lista_de_mesas'].append(nova_mesa)
        mesas['total_de_mesas'] += 1
        
    salvar_mesas(mesas)
    
    if quantia_de_mesas_a_adicionar == 1:
        print(f'\n✅ "{quantia_de_mesas_a_adicionar} Mesa foi adicionada com sucesso!')
    else:
        print(f'\n✅ "{quantia_de_mesas_a_adicionar} Mesas foram adicionadas com sucesso!')

    retorno_main()

def remover_mesa(mesas:dict):
    limpar_console()
    
    print('\n🌟 📝 REMOVER MESAS 🌟')
    print('-' * 50)
    
    quantia_de_mesas_a_remover = obter_int('🔢 Quantas mesas serão removidas: ', '⚠️ A quantidade de mesas não pode ser negativa. Tente novamente\n')
    
    for i in range(quantia_de_mesas_a_remover):
        mesas['lista_de_mesas'].pop()
        mesas['total_de_mesas'] -=1

    salvar_mesas(mesas)
    
    if quantia_de_mesas_a_remover == 1:
        print(f'\n✅ "{quantia_de_mesas_a_remover} Mesa foi removida com sucesso!')
    else:
        print(f'\n✅ "{quantia_de_mesas_a_remover} Mesas foram removidas com sucesso!')

    retorno_main()

def buscar_mesa_id(mesas:dict):
    limpar_console()
    
    print('\n🔍 📋 BUSCAR MESA POR ID 📋 🔍')
    print('-' * 50)

    buscar_mesa = obter_int("🔢 Informe o ID da mesa que deseja buscar: ", '⚠️ O ID não pode ser negativo. Tente novamente.')
    for mesa in mesas['lista_de_mesas']:
        if mesa['id'] ==  buscar_mesa:
            print(f"\n✅ Mesa encontrada!")
            print(f"🪑 ID da Mesa: {mesa['id']}")
            print(f'📌 Status: {mesa['status']} ')
            break
    else:
        print(f'\n❌ Mesa não encontrada. Verifique o ID e tente novamente.')
    
    retorno_main()

def listar_mesas(mesas:dict):
    limpar_console()
    
    print('\n🌟 📝 LISTANDO MESAS 🌟')
    print('-' * 50)
    
    for mesa in mesas['lista_de_mesas']:
        print(f"🪑 ID da Mesa: {mesa['id']}")
        print(f'📌 Status: {mesa['status']} ')
        print('-' * 50)

    retorno_main()
    
def editar_mesa(mesas:dict):
    limpar_console()
    
    print('\n🪑📝 EDITAR MESA 🪑📝')
    print('-' * 50)
    
    mesa_id = obter_int('🔢 Informe o número da mesa: ', '⚠️ O ID não pode ser negativo. Tente novamente.')
    
    mesa = next((mesa for mesa in mesas['lista_de_mesas'] if mesa_id == mesa['id']), None)
    
    if mesa:
        status_atual = mesa['status']
        print(f"\n📌 Status atual da mesa {mesa_id}: {mesa['status']}")
        
        opcoes_disponiveis = [v for v in STATUS_MESA.values() if v != status_atual]
        print("\n📋 Opções disponíveis:", " | ".join(opcoes_disponiveis))
        
        status = obter_texto("✏️  Informe o novo status da mesa: ").capitalize()
        
        mesa['status'] = status
        salvar_mesas(mesas)
        print(f'✅ Status da mesa {mesa_id} atualizado para {status}!' )
        
    else:
        print('❌ Mesa não encontrada.')