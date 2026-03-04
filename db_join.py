import sqlite3

def buscar_notas():
    conn = sqlite3.connect("meubanco.db")
    cursor = conn.cursor()
    cursor.execute("SELECT nota FROM alunos")
    dados = cursor.fetchall()
    conn.close() # sem isso o sqlite pode manter o arquivo bloqueado (lock), perder as alterações ou vazamento de recursos(ocupando memória do arquivo)
    return dados

 # cursor.fetchone() - Retorna somente 1 linha do banco 