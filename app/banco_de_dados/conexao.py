import sqlite3

def conectar():
    return sqlite3.connect("app/banco_de_dados/cafeteria.db")