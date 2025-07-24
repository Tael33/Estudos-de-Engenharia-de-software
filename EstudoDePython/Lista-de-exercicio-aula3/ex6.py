num1 = float(input('Digite um número: '))
num2 = float(input('Digite outro número: '))
print("Menu de opções:")
menuOpcao = input(
    'Escolha uma opção! \n"so" para soma; \n"su" para subtração; \n"pr" para produto; \n"di" para divisão; \nQual a sua opção?(so/su/pr/di): ')

if menuOpcao == 'so':
    print(f'A soma dos números é {num1 + num2}')
elif menuOpcao == 'su':
    if num1 > num2:
        print(f'A subtração dos números é {num1 - num2}')
    else:
        print(f'A subtração dos números é {num2 - num1}')
elif menuOpcao == 'pr':
    print(f'O produto dos Números é {num1 * num2}')
elif menuOpcao == 'di':
    if num2 == 0:
        print('ERRO: não é possível dividir por zero')
    else:
        print(f'A divisão dos números é {num1 / num2}')
else:
    print('Opção inválida! use apenas: (so/su/pr/di)')
