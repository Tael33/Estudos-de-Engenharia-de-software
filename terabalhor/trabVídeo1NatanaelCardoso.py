cont = 0
soma = 0

while cont < 5:
    num = float(input('Digite um numero: '))

    if num % 2 == 0:
        soma += num

    if num < 0 or num > 100:
        print('Fora de intervalo!')
    if num >= 0 and num <= 25:
        print('Intervalo [0,25]')
    if num > 25 and num <= 50:
        print('Intervalo [25, 50]')
    if num > 50 and num <= 75:
        print('Intervalo [50, 75]')
    if num > 75 and num <= 100:
        print('Intervalo [75, 100]')
    cont += 1

print(f'A soma dos números pares é: {soma}')
