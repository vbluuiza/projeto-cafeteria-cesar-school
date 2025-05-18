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
conexao.close()