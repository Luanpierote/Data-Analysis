import sqlite3
import pandas as pd

# Iniciar conexão
# conn = sqlite3.connect("meubanco.db") É INVIÁVEL COMPARTILHAR A CONEXÃO DO BANCO GLOBALMENTE 

# Criar um cursor

# Read
def buscar_dados():
    #  Inicia a conxão só quando eu preciso, e fecha automaticamente
    with sqlite3.connect("meubanco.db") as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM alunos")
        dados = cursor.fetchall() # Lendo o banco de dados; 
        return dados

# Create
def novo_registro(nome,nota):
    with sqlite3.connect("meubanco.db") as conn:
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO alunos(nome,nota,aprovacao) VALUES (?,?,?)",
            (nome,nota)
        )
        conn.commit() # Quando você edita algo no banco de dados

# Update
def atualizar_registro(id,nota,aprovacao):
    with sqlite3.connect("meubanco.db") as conn:
        cursor = conn.cursor()
        cursor.execute(
            "UPDATE alunos SET nota = ?,aprovacao = ? WHERE id = ?",
            (nota,aprovacao,id)
        )
        conn.commit()

# Delete
def deletar_registro(id):
      with sqlite3.connect("meubanco.db") as conn:
        cursor = conn.cursor()
        cursor.execute(
            "DELETE FROM alunos WHERE id = ?",
            (id,) # A vírgula é necessária porque o Python espera receber uma tupla
        )
        conn.commit()
  
 # cursor.fetchone() - Retorna somente 1 linha do banco 

def buscar_dados_csv():
   bd_imovel = pd.read_csv("models/house_prices.csv")
   bd_imovel = bd_imovel.iloc[:10,:8]
   return bd_imovel


buscar_dados_csv()