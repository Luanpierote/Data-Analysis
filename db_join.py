import sqlite3

# Iniciar conexão
# conn = sqlite3.connect("meubanco.db") É INVIÁVEL COMPARTILHAR A CONEXÃO DO BANCO GLOBALMENTE 

# Criar um cursor

# Read
def buscar_notas():
    #  Inicia a conxão só quando eu preciso, e fecha automaticamente
    with sqlite3.connect("meubanco.db") as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT nome,nota FROM alunos")
        dados = cursor.fetchall() # Lendo o banco de dados; 
        return dados

# Create
def novo_registro(nome,nota):
    with sqlite3.connect("meubanco.db") as conn:
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO alunos(nome,nota) VALUES (?,?)",
            (nome,nota)
        )
        conn.commit() # Quando você edita algo no banco de dados

# Update
def atualizar_registro(id,nota):
    with sqlite3.connect("meubanco.db") as conn:
        cursor = conn.cursor()
        cursor.execute(
            "UPDATE alunos SET nota = ? WHERE id = ?",
            (nota,id)
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