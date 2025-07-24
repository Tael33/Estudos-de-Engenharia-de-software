# Crie um código em que o usuário entrará com os dados de 3 alunos, com CGU, nome e médis final e armazene em uma matriz, depois disso, imprima os dados de cada aluno, linha por linha, e imprima a média final de cada aluno.

alunos = []
cont = 0
while cont < 3:
    aluno = []
    cgu = input("Digite o CGU do aluno: ")
    nome = input("Digite o nome do aluno: ")
    media = float(input("Digite a média final do aluno: "))
    aluno.append(cgu)
    aluno.append(nome)
    aluno.append(media)
    alunos.append(aluno)
    cont += 1

print(alunos[0][0], alunos[0][1], alunos[0][2])
print(alunos[1][0], alunos[1][1], alunos[1][2])
print(alunos[2][0], alunos[2][1], alunos[2][2])
