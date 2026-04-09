# Objetivo: Usar este ambiente para efetuar as operações matemáticas ✅
# Resultado: Tecnicamente correto, modelo mal fundamentado( Scartter é melhor para visualizar o rendimeto dos alunos ao longo do tempo), resultado impreciso por falta de dados e assimilação

from db_join import buscar_notas

import pandas as pd
import statsmodels.api as sm

#  Módulo que cria o gráfico /esse módulo está instalado dentro do ecossistema virtual
import matplotlib.pyplot as plt

notas = buscar_notas()
array = []

soma = sum(nota[0] for nota in notas) #função que efetua a soma de uma lista.
 #O indice é 0, porque só existe 1 elemento dentro da tupla(Ex.: (8.5))

for nota in notas:
   array.append(nota[0])

media = soma/len(notas)

"""
Regressão Linear básica com Statsmodel e Pandas:

Notas em função dos anos cursados( Da turma inteira)
//Imcompleto

"""
notas = [n[0] for n in notas]
ano = range(2021,2026)

df = pd.DataFrame({
    "ano": ano,
    "nota": notas
})

y = df["nota"]
X = df[["ano"]]

X = sm.add_constant(X)

modelo = sm.OLS(y, X)
resultado = modelo.fit()

print(resultado.summary())


plt.title("Sala de Aula")
plt.ylabel("Quantidade de Alunos")
plt.xlabel("Notas")
plt.yticks(range(0,5))

plt.text(0.5,0.6,
         f"média:{media}",
         transform=plt.gca().transAxes,
         ha="center"
)

plt.hist(array)
plt.show()


print(f'A soma das notas dos alunos é: {soma}')
print(f'A média dos alunos é: {media}') 
