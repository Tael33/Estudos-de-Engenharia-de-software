B = float(input('Digite o valor da base: '))
H = float(input('Digite o valor da altura: '))

if B == H:
    print('É um quadrado perfeito!')
else:
    print('É um retângulo!')
    if B > H:
        print('A base é maior que a altura!')
    else:
        print('A altura é maior que a base!')
