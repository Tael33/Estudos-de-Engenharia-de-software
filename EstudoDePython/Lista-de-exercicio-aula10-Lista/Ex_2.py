# Arquivo gerado automaticamente
cont = 0
fim = int(input('Digite um número: (0 para sair) '))
list = []
while fim != 0:
    list.append(fim)
    fim = int(input('Digite um número: (0 para sair) '))
print(list)

while cont < len(list):
    print(f'O número {list[cont]} na posição {cont}')
    cont += 1
