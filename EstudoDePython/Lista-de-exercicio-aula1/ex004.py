salario = float(input('Digite o salário: R$ '))
kwUsado = float(input('Digite a quantidade de KW usado: '))
custoKw = salario / 100
valorConta = kwUsado * custoKw
print(f'O valaor da conta de energia é R$ {valorConta:.2f}.')
