sexo = input('Qual é o seu sexo? (m/f): ')
turno = input('Qual é o seu turno? (m/v): ')

if sexo == 'm' and turno == 'm':
    print('Bom dia, querido aluno')
elif sexo == 'm' and turno == 'v':
    print('Boa tarde, querido aluno')
elif sexo == 'f' and turno == 'm':
    print('Bom dia, querida aluna')
elif sexo == 'f' and turno == 'v':
    print('Boa tarde, querida aluna')
