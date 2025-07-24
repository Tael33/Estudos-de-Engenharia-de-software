num1 = int(input('Digite um numero: '))
num2 = int(input('Digite outro número: '))
num3 = int(input('Digite outro número: '))
num4 = int(input('Digite outro número:'))

quantZero = int()

if num1 == 0:
    quantZero += 1
if num2 == 0:
    quantZero += 1
if num3 == 0:
    quantZero += 1
if num4 == 0:
    quantZero += 1

print(f'A quantidade de zeros é: {quantZero}')
