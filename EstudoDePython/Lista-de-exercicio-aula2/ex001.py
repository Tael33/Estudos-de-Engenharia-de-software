n1 = int(input("Digite um número: "))
n2 = int(input("Digite outro número: "))
soma = n1 + n2
print(f'A soma é {soma}')

if soma % 2 == 0:
    print(f'A metade da soma é {soma / 2}')
else:
    print(f'A soma é IMPAR')
