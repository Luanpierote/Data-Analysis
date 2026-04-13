from db_join import buscar_dados,novo_registro,atualizar_registro,deletar_registro
from flask import Flask,jsonify
from flask_cors import CORS

dados = buscar_dados()

#O indice é 0, porque só existe 1 elemento dentro da tupla(Ex.: (8.5))
soma = sum(float(linha[2]) for linha in dados) #função que efetua a soma de uma lista.
 
media = soma/len(dados[1])  


for id,nome,nota,aprovacao in buscar_dados():
    if nota >= 6.0:
        atualizar_registro(id,nota,'Aprovado')
    else:
        atualizar_registro(id,nota,'Reprovado')

""" LIGANDO O SERVIDOR """
app = Flask(__name__)
CORS(app)

@app.route("/usuarios")
def usuarios():
    return jsonify(dados)

# cria uma aplicação web
app.run(debug=True)