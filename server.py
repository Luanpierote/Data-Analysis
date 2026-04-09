from db_join import buscar_notas,novo_registro,atualizar_registro,deletar_registro
from flask import Flask,jsonify

dados = buscar_notas()

#O indice é 0, porque só existe 1 elemento dentro da tupla(Ex.: (8.5))
soma = sum(float(nota) for _,nota in dados) #função que efetua a soma de uma lista.
 
media = soma/len(dados[1])  

atualizar_registro(6,6.5)

deletar_registro(5)

""" LIGANDO O SERVIDOR """
app = Flask(__name__)

@app.route("/usuarios")
def usuarios():
    return jsonify(dados)

# cria uma aplicação web
app.run(debug=True)