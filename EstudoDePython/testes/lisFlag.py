numeros = []

numero = int(input("Digite um número: "))

while numero != 0:

    numero = int(input("Digite um número: "))

    numeros.append(numero)

i = 0
while i < len(numeros):
    print(numeros[i][0])
    i += 1
