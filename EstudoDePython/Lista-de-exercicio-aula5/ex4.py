quantPessoas = int(input('Quantas pessoas assitiram a dança: '))

pessoasS = 0
pessoasN = 0
cont = 0

while cont < quantPessoas:
    gosto = input('Você gostou da apresentação? (s/n): ')

    if gosto == 's':
        pessoasS += 1
    else:
        pessoasN += 1
if pessoasS > pessoasN:
    print(f'A maioria das pessoas gostaram: com {pessoasS}')
elif pessoasN > pessoasS:
    print(f'A maioria das pessoas nâo gostaram: com {pessoasN}')
elif pessoasN == pessoasS:
    print(f'Esta impatado! com {pessoasN + pessoasS}')
