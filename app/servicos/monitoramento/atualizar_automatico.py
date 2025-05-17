import time
from datetime import datetime
from app.repositorios.repositorio_pedidos import carregar_pedidos, salvar_pedidos
from app.repositorios.repositorio_mesas import carregar_mesas, salvar_mesas
from app.utils.utilitarios_global import STATUS_PEDIDO, STATUS_MESA

def atualizar_status(pedidos, mesas):
    
    for pedido in pedidos["pedidos"]:
        status_atual = pedido["status"]

        if status_atual not in STATUS_PEDIDO.values():
            continue

        status_atual_index = next((k for k, v in STATUS_PEDIDO.items() if v == status_atual), None)

        if status_atual_index in [3, 4]:
            continue

        proximo_index = status_atual_index + 1

        if proximo_index in STATUS_PEDIDO:
            novo_status = STATUS_PEDIDO[proximo_index]
            pedido["status"] = novo_status
            # print(f"\n📦 Pedido da mesa {pedido['mesa']} atualizado para: {novo_status}")

            if proximo_index == 3:  
                mesa = next((m for m in mesas["lista_de_mesas"] if m["id"] == pedido["mesa"]), None)
                if mesa:
                    mesa["status"] = STATUS_MESA[0]
                    # print(f"🪑 Mesa {mesa['id']} liberada automaticamente.")

    salvar_pedidos(pedidos)
    salvar_mesas(mesas)
    
def iniciar_monitoramento():
    # print("\n⏳ Aguardando 30 segundos para iniciar o monitoramento automático...")
    time.sleep(30)
    while True:
        pedidos = carregar_pedidos()
        mesas = carregar_mesas()
        atualizar_status(pedidos, mesas)
        time.sleep(15)


