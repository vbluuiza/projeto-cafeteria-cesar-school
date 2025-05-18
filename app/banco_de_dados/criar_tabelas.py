from conexao import conectar
import sqlite3

conexao = conectar()
cursor = conexao.cursor()

cursor.execute('''
                CREATE TABLE IF NOT EXISTS cardapio (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nome TEXT(50) NOT NULL,
                    descricao TEXT (300),
                    ingredientes TEXT(150),
                    preco TEXT(10) NOT NULL,
                    subcategoria TEXT(50) NOT NULL,
                    categoria TEXT(50) NOT NULL
                )
               ''')

conexao.commit()


cursor.execute('''
               CREATE TABLE IF NOT EXISTS mesa (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    status TEXT(50) NOT NULL
                    
                )
               ''')

conexao.commit()
cursor.execute('''
                CREATE TABLE IF NOT EXISTS pedidos (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    mesa_id INTERGER NOT NULL,
                    preco_total TEXT (10) NOT NULL,
                    observacao TEXT (300),
                    status TEXT(50) NOT NULL,
                    FOREIGN KEY (mesa_id) REFERENCES mesa(id)
                )
               ''')

conexao.commit()
cursor.execute('''
                CREATE TABLE IF NOT EXISTS itens_pedido (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    pedido_id INTERGER NOT NULL,
                    cardapio_id INTERGER NOT NULL,
                    quantidade INTEGER NOT NULL,
                    preco_unitario TEXT (10) NOT NULL,
                    FOREIGN KEY (pedido_id) REFERENCES pedidos(id),
                    FOREIGN KEY (cardapio_id) REFERENCES cardapio(id)
                )
               ''')
conexao.commit()
conexao.close()