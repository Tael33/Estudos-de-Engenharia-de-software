cont = 0
somaLucro = 0

while cont < 5:
    precoCompra = float(input('Digite o preço de compra: '))
    precoVenda = float(input('Digite o preço de venda: '))

    lucro = precoCompra - precoVenda

    print(f'O luccro é R$ {lucro}')
    somaLucro += lucro

    cont += 1

print(f'A média de lucro é R$ {somaLucro/5}')
