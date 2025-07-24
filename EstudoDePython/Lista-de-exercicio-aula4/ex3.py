print('Digite o seu peso e sua altura para saber seu Índice de Massa Corporal(IMC):')

peso = float(input('Qual o seu peso em (Kg): '))
altura = float(input('Qual a suaa altura em: '))

icm = peso / (altura**2)
print(icm)

if icm <= 18:
    print('(ICM): Abaixo do peso!')
elif icm >= 18.5 and icm <= 24.9:
    print('(ICM): Peso normal!')
elif icm >= 25 and icm <= 29.9:
    print('(ICM): Sobrepeso!')
elif icm > 30:
    print('(ICM): Obesidade!')
