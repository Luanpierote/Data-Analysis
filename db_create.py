# objetivo: Tendencia Central - Média,mediana,moda

# operação: use o módulo math se precisar

import sqlite3

conn = sqlite3.connect("meubanco.db")
cursor = conn.cursor() # cursor é o objeto que executa comandos SQL e navega pelos resultados.

cursor.execute("""
CREATE TABLE IF NOT EXISTS alunos(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT UNIQUE ,
        nota REAL 
)
""")
# UNIQUE foi usado para não permitir dados repetidos

cursor.execute("INSERT INTO alunos (nome,nota) VALUES (?,?)",("Luan",8.5))
cursor.execute("INSERT INTO alunos (nome,nota) VALUES (?,?)",("Cardoso",7.6))
cursor.execute("INSERT INTO alunos (nome,nota) VALUES (?,?)",("Matheus",8.6))
cursor.execute("INSERT INTO alunos (nome,nota) VALUES (?,?)",("André",7.2))
cursor.execute("INSERT INTO alunos (nome,nota) VALUES (?,?)",("Richard",6.5))

conn.commit() # Salvar as alterações/gravar os dados

cursor.execute("SELECT * FROM alunos")
dados = cursor.fetchall() # método que transforma cada linha de uma tabela em uma tupla, e coloca esses elementos dentro de um array

for linha in dados:
    print(linha)

conn.close()
# print(sqlite3.sqlite_version_info) O sqlite3 é nativo do Python
