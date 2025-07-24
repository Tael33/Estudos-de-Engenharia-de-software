litro = float(input('Digite a quantidade de litros de combustível: '))
print('O preço do litro de gasolina é R$ 7,00')
print('O preço do litro de álcool é R$ 5,00')
tipo = input(
    'Digite o tipo de combustível: ("A" para álcool ou "G" para gasolina) ')

if tipo == 'A' or tipo == 'a':
    preco = litro * 5
    if litro >= 20 and litro <= 30:
        Npreco = preco - (preco * 0.05)
        print(f'O preço a ser pago com 5% de desconto é R$ {Npreco}')
    elif litro > 30:
        Npreco = preco - (preco * 0.1)
        print(f'O preço a ser pago com 10% de desconto é R$ {Npreco}')
    else:
        print(f'O preço a ser pago é R$ {preco}')
elif tipo == 'g' or tipo == 'G':
    preco = litro * 7
    if litro >= 20 and litro <= 30:
        Npreco = preco - (preco * 0.05)
        print(f'O preço a ser pago com 5% de desconto é R$ {Npreco}')
    elif litro > 30:
        Npreco = preco - (preco * 0.1)
        print(f'Opreço a ser pago com 10% de desconto é R$ {Npreco}')
    else:
        print(f'O preço a ser pago é R$ {preco}')
elif tipo != 'A' or tipo != 'a' or tipo != 'G' or tipo != 'g':
    print('Código inválido, tente novamente! Usando "A" ou "G"')
