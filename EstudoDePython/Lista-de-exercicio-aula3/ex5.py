ladoA = float(input('Digite o valor do lado A: '))
ladoB = float(input('Digite o valor do lado B: '))
ladoC = float(input('Digite o valor do lado C: '))

if ladoA and ladoB and ladoC > 0:
    if ladoA == ladoB == ladoC:
        print('Triângulo Equilatero')
    elif ladoA == ladoB or ladoA == ladoC or ladoB == ladoC:
        print('Triângulo Isósceles')
    else:
        print('Triângulo Escaleno')
else:
    print('Nenhum número pode ser zero para ser um triângulo!')
