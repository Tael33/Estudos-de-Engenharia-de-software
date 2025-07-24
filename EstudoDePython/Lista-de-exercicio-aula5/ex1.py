cont = 0
soma = 0
zero = 0
mediaNegativo = 0
contN = 0

while cont < 6:
    num = int(input('Digite um numero:'))

    if num > 0:
        print(f'{num}: É positivo!')
        soma += num
    elif num < 0:
        contN += 1
        print(f'{num}: É Négativo!')
        mediaNegativo += num
    else:
        print(f'{num}: É iqual a zero!')
        zero += 1


print(f'A quatidade de zeros é: {zero}')
print(f'A soma dos números positivos é: {soma}')
print(f'A média dos número negativos é: {mediaNegativo/contN}')
