from db_join import buscar_notas
import math

notas = buscar_notas()

soma = sum(nota[0] for nota in notas) #função que efetua a soma de uma lista.
 #O indice é 0, porque só existe 1 elemento dentro da tupla(Ex.: (8.5))

media = soma/notas.__len__()

print(f'A soma das notas dos alunos é: {soma}')
print(f'A média dos alunos é: {media}')