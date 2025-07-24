'''
1. O programa abaixo insere 10 números aleatórios, entre -10 e 10 (inclusive os dois), em uma lista.
import random
numeros = []
i=0
while i < 10:
numeros.append(random.randint(-10,10))
i = i + 1
print("Numeros:", numeros)
Continue o código para realizar as seguintes ações:
● (0,2) Imprima a soma dos elementos que estão nas posições pares da lista.
● (0,2) Imprima a lista de trás para frente, sem utilizar índices negativos.
● (0,3) Imprima o menor número negativo presente na lista. Caso não existam números negativos,
informe ao usuário.
● (0,3) Imprima o maior número entre os armazenados nas 5 primeiras posições da lista.
'''
import random
numeros = []
i = 0
while i < 10:
    numeros.append(random.randint(-10, 10))
    i = i + 1
print("Numeros:", numeros)

# ● (0,2) Imprima a soma dos elementos que estão nas posições pares da lista.
SomaPares = 0
i = 0
while i < len(numeros):
    if i % 2 == 0:
        SomaPares += numeros[i]
    i += 1
print("Soma dos elementos nas posições pares:", SomaPares)

# ● (0,2) Imprima a lista de trás para frente, sem utilizar índices negativos.

inverso = []
i = len(numeros) - 1
while i >= 0:
    inverso.append(numeros[i])
    i -= 1
print(inverso)

# ● (0,3) Imprima o menor número negativo presente na lista. Caso não existam números negativos, informe ao usuário.

menor = 0
i = 0
while i < len(numeros):
    if numeros[i] < 0:
        if numeros[i] < menor:
            menor = numeros[i]
    i += 1
if menor < 0:
    print("Menor número negativo:", menor)
else:
    print("Não existem números negativos na lista.")

# (0,3) Imprima o maior número entre os armazenados nas 5 primeiras posições da lista.

i = 0
maior = 0
while i < 5:
    if numeros[i] > maior:
        maior = numeros[i]
    i += 1
print("Maior número entre os armazenados nas 5 primeiras posições:", maior)
