# ☕ Sistema de Gestão para Cafeteria

📌 **Versão:** 1.0  
🗓️ **Última atualização:** Maio de 2025  

Um sistema desenvolvido em Python com o objetivo de gerenciar as operações internas de uma cafeteria. O projeto contempla funcionalidades completas de controle de **cardápio**, **pedidos**, **mesas** e uma rotina automática para **atualização de status de pedidos e liberação de mesas**.

## 🧱 Tecnologias utilizadas

- `Python 3.11+`
- `JSON` como banco de dados simples
- `Threading` para monitoramento automático
- Estrutura modular por pastas (`serviços`, `repositórios`, `dados`, etc.)

## ⚙️ Funcionalidades

### 🧾 Cardápio (CRUD)

- Cadastrar itens (prato, bebida, sobremesa)
- Listar cardápio por categoria
- Editar e remover itens
- Buscar item do cardápio

### 🪑 Mesas (CRUD)

- Cadastrar e remover mesas
- Editar status das mesas (`disponível`, `ocupada`, `em espera`)
- Buscar mesa por ID
- Listar todas as mesas

### 📦 Pedidos (CRUD)

- Criar pedidos vinculados a mesas
- Editar pedidos (itens, observações, status)
- Remover pedidos
- Listar todos os pedidos
  

### 🔄 Monitoramento Automático

- Inicia com atraso de 30 segundos
- A cada 15 segundos, atualiza o status dos pedidos:
    
    ```
    Pedido Aprovado → Em preparo → Pronto → Entregue
    ```
    
- Libera automaticamente a mesa ao finalizar o pedido (`Entregue`

---

## 🚀 Como executar

1. Clone o repositório:
    
    ```bash
    git clone https://github.com/seu-usuario/projeto-cafeteria
    ```
    
2. Execute o sistema:
    
    ```bash
    python app/main.py
    ```
    

> O monitoramento automático começará sozinho após 30 segundos e continuará executando em segundo plano.
> 

---

## 👨‍💻 Autores

Projeto desenvolvido por estudantes do curso de **Análise e Desenvolvimento de Sistemas**:

- Luiza Vieira
- Marcello
- Gabriel
- Lucca
- Eliziane
- Laiza

Desenvolvido como projeto para a disciplina *Fundamentos da Programação (FP)*
