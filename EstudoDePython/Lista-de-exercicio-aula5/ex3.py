mulheres = 0
homens = 0
idadeMedia = 0
cont = 0

while cont < 15:
    idade = int(input('Digete a idade: '))
    nacionalidade = input('Digite a nacionalidade: ')
    sexo = input('Qual o sexo f/m')

    if idade > 18 and sexo == 'f':
        mulheres += 1
    if sexo == 'm' and nacionalidade == 'brasileiro' and idade >= 20 and idade <= 30:
        homens += 1
    idadeMedia += idade
    cont += 1
print(f'Quantidade de mulheres maiores de idade: {mulheres}')
print(f'Quantidade de homens brasileiros entre 20 e 30 anos: {homens}')
print(f'Média das idades: {idadeMedia/15}')
