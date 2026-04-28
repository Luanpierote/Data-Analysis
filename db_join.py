import sqlite3
import pandas as pd
import numpy as np

# Iniciar conexão
# conn = sqlite3.connect("meubanco.db") É INVIÁVEL COMPARTILHAR A CONEXÃO DO BANCO GLOBALMENTE 

# Criar um cursor

bd_imovel = pd.read_csv("models/house_prices.csv")

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

def buscar_dados_tabela_csv():
    bd_imovel["date"] = pd.to_datetime(bd_imovel["date"]).dt.to_period("M").astype(str)
    return bd_imovel.iloc[:10, :8].to_dict(orient='records')

def buscar_dados_grafico_csv():
    bd_subset = bd_imovel.copy()
    print(bd_subset)
    # Coluna do tipo Datetime
    bd_subset["date"] = pd.to_datetime(bd_subset["date"])
    
    # Agrupando pelo período mensal e calculando a média do preço/ todos os dados que pertencem ao mesmo mês são colocados no mesmo lugar
    # Ex: Grupo 2026-01: [65.000, 64.000]
    bd_agregado = bd_subset.groupby(bd_subset["date"].dt.to_period("M"))
    # O pandas "joga" o índice de volta para dentro do DataFrame como uma coluna comum, e transforma em uma lista de objetos comum
    bd_agregado = bd_agregado["price"].mean().reset_index()

    # Converta de volta para string para o Chart.js entender
    bd_agregado["date"] = bd_agregado["date"].astype(str)
    
    return  bd_agregado.to_dict(orient='records')
    

