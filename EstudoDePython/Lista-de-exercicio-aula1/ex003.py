precoPorQuilo = 30.00
pesoPrato = 0.1
pesoRefeicao = float(input('Digite o peso da refeição: '))
procoTotal = pesoRefeicao - pesoPrato

print(f'O valor total da refeição é R$ {procoTotal * precoPorQuilo:.2f}.')
