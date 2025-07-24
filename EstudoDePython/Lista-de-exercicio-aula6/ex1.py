media_salario = 0
salarioMaior = 0
salarioMenor = 9999999
contPessoas = 0

nome = input('Qual o nome do funcionário: ')

while nome != 'fim':

    salario = int(input('Qual o salário do funcionário: '))
    contPessoas += 1
    somaSalario += salario
    print(f'O nome do fincionário é {nome}')
    print(f'O salário do fincionário é R${salario}')

    if salario > salarioMaior:
        salarioMaior = salario
    if salario < salarioMenor:
        salarioMenor = salario

    nome = input('Qual o nome do funcionário: ')

media_salario = somaSalario / contPessoas
print(f'A média dos salários dos funcionários é {media_salario:.2f}')
