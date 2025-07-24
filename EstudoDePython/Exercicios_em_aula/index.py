quntProduto = int(input('Qual a quantidade de produtos '))
valorProdutos = float('Qual o valor dos produtos: ')

total = quntProduto * valorProdutos

if quntProduto >= 15 or valorProdutos >= 1000:
    total = total - (total * 0.15)
    print('Desconto')
