'''Numa fábrica trabalham homens e mulheres divididos em duas classes:
- A – os que fazem até 100 peças por mês;
- B – os que fazem mais de 100 peças por mês.
Os operários da classe ‘A’ recebem apenas o salário-mínimo mais 2.00 por peça e os operários da classe
‘B’ recebem salário-mínimo mais R$ 2.50 por peça.
Fazer um algoritmo que:
1 - Leia inicialmente o valor do salário-mínimo;
2 - Leia várias linhas contendo o nome do operário e quantas peças ele fabricou no mês. A última linha,
que servirá de flag (condição de parada), terá o nome do operário igual a “sair”.
3 - Apresente a folha de pagamento do mês, com as seguintes informações:
a. O nome, a classe e o salário de cada operário;
b. O valor do maior salário;
c. A somatória dos salários dos operários.'''

nome = ''
pecasMes = 0
salarioMaior = 0
salarioMenor = 999999
salarioMinimo = 0
somaSalario = 0
nomeMaiorSalario = ''
nomeMenorSalario = ''
classMaiorSalario = ''
classMenorSalario = ''
classe = ''

nome = input('Qual o nome do funcionário: ')

while nome != 'fim':

    salarioMinimo = float(input('Qual o salário mínimo do funcionário: '))
    pecasMes = int(input('Quantas peças ele fabricou no mês: '))
    print(f'O nome do fincionário é {nome}')

    if pecasMes > 100:
        salario = salarioMinimo + (pecasMes * 2.5)
        classe = 'B'
        print(f'Classe B com {pecasMes} peças e salário de {salario}')
    else:
        salario = salarioMinimo + (pecasMes * 2)
        classe = 'A'
        print(f'Classe A com {pecasMes} peças e salário de {salario}')

    if salario > salarioMaior:
        salarioMaior = salario
        nomeMaiorSalario = nome
        classMaiorSalario = classe
    if salario < salarioMenor:
        salarioMenor = salario
        nomeMenorSalario = nome
        classMenorSalario = classe

    somaSalario += salario

    nome = input('Qual o nome do funcionário: ')

print(
    f'O maior salário foi de {salarioMaior} do funcionário {nomeMaiorSalario} da classe {classMaiorSalario}')
print(
    f'O menor salário foi de {salarioMenor} do funcionário {nomeMenorSalario} da classe {classMenorSalario}')
print(f'A soma dos salários dos funcionários foi de {somaSalario}')
