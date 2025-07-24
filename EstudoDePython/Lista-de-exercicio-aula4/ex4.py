usuario = input(
    'Qual a sua categoria ((es)Estudande, (ps)Professor, (pf)Proficional): ')
traducao = input('Você quer tradução simutânea (s/n): ')
curso = input('Você quer mini-cursos (s/n): ')
valor = float()
if usuario:
    if usuario == 'es' or usuario == 'ps':
        valor += 100
    else:
        valor += 150
if traducao == 's':
    valor += 20
if curso == 's':
    valor += 50

print(
    f'Conclusão:\nVocê é: {usuario}\nTradução simutânea: {traducao}\nMini-curso: {curso}\nO valor a ser pago é: {valor}')
