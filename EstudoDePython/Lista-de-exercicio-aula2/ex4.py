num = int(input("Digite um número: "))

if num > 0:
    print(f'O número {num} é positivo! \nO seu dobro é {num * 2}')
elif num < 0:
    print(f'O número {num} é negativo!')
    if num % 2 == 0:
        print('É par!')
    else:
        print('É ímpar!')
else:
    print(f'O número {num} é igual a zero!')
