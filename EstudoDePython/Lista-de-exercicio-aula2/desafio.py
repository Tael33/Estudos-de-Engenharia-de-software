pessoa1 = input("Digite o nome da primeira pessoa: ")

print('Informe a data de nascimento')

dia1 = int(input('Dia:'))
mes1 = int(input('Mês:'))
ano1 = int(input('Ano:'))

pessoa2 = input("Digite o nome da segunda pessoa: ")

print('Informe a data de nascimento')

dia2 = int(input('Dia:'))
mes2 = int(input('Mês:'))
ano2 = int(input('Ano:'))

if dia1 == dia2 and mes1 == mes2 and ano1 == ano2:
    print('As pessoas possuem a mesma idade')
elif ano1 == ano2 and mes1 == mes2 and dia1 < dia2:
    print(f'{pessoa1} é mais velho(a) que {pessoa2} por diferença de dias')
elif ano1 == ano2 and mes1 == mes2 and dia1 > dia2:
    print(f'{pessoa2} é mais velho(a) que {pessoa1} por diferença de dias')
elif ano1 == ano2 and mes1 < mes2:
    print(f'{pessoa1} é mais velho(a) que {pessoa2} por diferença de mês')
elif ano1 == ano2 and mes1 > mes2:
    print(f'{pessoa2} é mais velho(a) que {pessoa1} por diferença de mês')
elif ano1 < ano2:
    print(f'{pessoa1} é mais velho(a) que {pessoa2} por dirença de anos')
else:
    print(f'{pessoa2} é mais velho(a) que {pessoa1} por diferença de anos')
