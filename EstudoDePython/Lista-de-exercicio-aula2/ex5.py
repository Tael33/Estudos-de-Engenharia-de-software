num1 = int(input('Digite um número: '))
num2 = int(input('digite outro número: '))
codigo = input(
    'digite um codigo: ("c" para crecente ou "d" para decrescente) ')

if codigo == 'c' or codigo == 'C':
    if num1 < num2:
        print(f'{num1}, {num2}')
    else:
        print(f'{num2}, {num1}')
elif codigo == 'd' or codigo == 'D':
    if num1 < num2:
        print(f'{num2}, {num1}')
    else:
        print(f'{num1}, {num2}')
else:
    print('Código inválido, tente novamente! Usando "c, C" ou "d, D"')
