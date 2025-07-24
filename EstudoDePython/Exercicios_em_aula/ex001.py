num1 = float(input('Digite um número:'))
num2 = float(input('Digite outro número:'))

if num1 == num2:
    print('Numeros iguais')
else:
    print('Número diferentes')
    if num1 > num2:
        print('O primeiro número é maior')
    else:
        print('O segundo número é maior')
