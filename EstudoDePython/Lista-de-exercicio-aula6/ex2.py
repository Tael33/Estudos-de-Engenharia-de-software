'''Faça um algoritmo que leia o preço, o nome do artista e a categoria (Escultura ou Quadro) de um número
indeterminado de obras que foram expostas em feira de artes, sendo que a leitura deverá ser encerrada
quando o usuário digitar um preço menor ou igual a zero. Calcule e imprima:
a. o nome do artista da escultura mais cara, considerando que não houve empate;
b. a categoria da obra mais barata.
'''

escultura_mais_cara = ''
preco_escultura_mais_cara = 0
obra_mais_barata = ''
preco_obra_mais_barata = 9000000000
categoria = ''

preco = float(input("Digite o preço da obra: "))

while preco > 0:
    nome_artista = input("Digite o nome do artista: ")
    categoria = input("Digite a categoria (Escultura ou Quadro): ")

    if categoria == "Escultura" and preco > preco_escultura_mais_cara:
        escultura_mais_cara = nome_artista
        preco_escultura_mais_cara = preco

    if preco < preco_obra_mais_barata:
        obra_mais_barata = categoria
        preco_obra_mais_barata = preco

    preco = float(input("Digite o preço da obra: "))

print("O nome do artista da escultura mais cara é:", escultura_mais_cara)
print("O preço da escultura mais cara é:", preco_escultura_mais_cara)
print("A categoria da obra mais barata é:", obra_mais_barata)
print("O preço da obra mais barata é:", preco_obra_mais_barata)
