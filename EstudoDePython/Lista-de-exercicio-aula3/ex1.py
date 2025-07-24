cinto = input('Está usando cinto de segurança (s/n)? ')
sobrio = input('Está sóbrio (s/n)? ')
revisão = input('Seu carro está em dia com a revisão (s/n)? ')
if cinto == 's' and sobrio == 's' and revisão == 's':
    print('Você está autorizado a dirigir')
else:
    print('Você não está autorizado a dirigir')