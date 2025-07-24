# Arquivo gerado automaticamente
list = []
maiores = []
cont = 0
media = 0
while len(list) < 5:
    list.append(float(input(f'Digite a média do aluno: ')))
while cont < len(list):
    media += list[cont]
    cont += 1
media = media / len(list)
print(f'A média da turma é {media}')
cont = 0
while cont < len(list):
    if list[cont] > media:
        maiores.append(list[cont])
    cont += 1
print(f'A quantidade de alunos acima da média é {len(maiores)}')


'''medias = [float(input(f'Digite a média do aluno {i + 1}: ')) for i in range(5)]

media_turma = sum(medias) / len(medias)
print(f'A média da turma é {media_turma:.2f}')

acima_da_media = [media for media in medias if media > media_turma]
print(f'A quantidade de alunos acima da média é {len(acima_da_media)}')'''
