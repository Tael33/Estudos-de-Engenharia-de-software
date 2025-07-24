# Arquivo gerado automaticamente
list = []
cont = 0
somaPar = 0
while len(list) < 6:

    list.append(int(input('Digite um número: ')))

while cont < len(list):
    print(f'O número {list[cont]} na posição {cont}')

    if list[cont] % 2 == 0:
        somaPar += list[cont]
    cont += 1

print(f'A soma dos números pares é {somaPar}')
print(list[0])
print(list[1])
print(list[2])
