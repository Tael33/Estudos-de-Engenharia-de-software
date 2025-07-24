# Arquivo gerado automaticamente
lista = [10, 5, 8, 20, 50, 10, 5, 8, 8, 60, 10, 5, 5, 3, 50]
cont = 0
numMaior = 0
somaPar = 0
while cont < len(lista):
    if lista[cont] > numMaior:
        numMaior = lista[cont]
    if lista[cont] % 2 == 0:
        somaPar += lista[cont]
        print(f'O número {lista[cont]} da posição {cont} é par')
    cont += 1
cont = 0
print('\n')
while cont < 5:
    print(f'O número {lista[cont]} na posição {cont}')
    cont += 1
print('\n')
print(f'O maior numero da lista é {numMaior}')
print(f'A soma dos pares é {somaPar}')
