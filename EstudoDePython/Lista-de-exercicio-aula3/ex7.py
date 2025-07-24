idade = int(input('Qual a idade: '))
peso = float(
    input('Coloque o peso em quilo para saber quantas gotas de medicamendo deve tomar: '))

if idade >= 12 and peso <= 60:
    gotas = 30
elif idade >= 12 and peso > 60:
    gotas = 40
elif idade < 12 and peso <= 10:
    gotas = 5
elif idade < 12 and peso <= 20:
    gotas = 10
elif idade < 12 and peso <= 30:
    gotas = 15
elif idade < 12 and peso > 30:
    gotas = 20

print(f'O paciente deve tomar {gotas} gotas por dose!')
