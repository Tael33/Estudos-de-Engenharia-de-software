quantidadeLapis = int(input('Digite a quantidade de pacotes de lapis: '))
quantidadeCanetas = int(input('Digite a quantidade de pacotes de canetas: '))

valorPacoteLapis = 8
valorPacoteCanetas = 6.5

valorLapis = quantidadeLapis * valorPacoteLapis
valorCanetas = quantidadeCanetas * valorPacoteCanetas
valorTotal = valorLapis + valorCanetas

print(f'O valor total a pagar é R$ {valorTotal:.2f}.')
