num1 = int(input('Digite um número: '))
num2 = int(input('Digite outro número: '))
num3 = int(input('Digite outro número: '))

if num1 and num2 and num3 != 0:
    if num1 and num2 and num3 > 0:
        print(f'O produto dos números é {num1 * num2 * num3}: ')
    elif num1 > 0 or num2 > 0 or num3 > 0:
        print(f'A soma dos números é {num1 + num2 + num3}: ')
    elif num1 and num2 and num3 < 0:
        print(f'A média dos números é {(num1 + num2 + num3) / 3}: ')
else:
    print('Nenhum número pode ser zero')
