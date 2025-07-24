quantidadeCaixasClipsPlastico = int(
    input('Digite a quantidade de caixas de clips de Plastico: '))
quantidadeCaixasClipsMetal = int(
    input('Digite a quantidade de caixas de clips de Metal: '))
clipsPlastico = 5
clipsMetal = 10
valorClipsPlastico = quantidadeCaixasClipsPlastico * clipsPlastico
valorClipsMetal = quantidadeCaixasClipsMetal * clipsMetal
valorTotal = valorClipsPlastico + valorClipsMetal
print(
    f'O valor das caixas de clips de Plastico é R$ {valorClipsPlastico:.2f}\nO valor das caixas de clips de metal é R$ {valorClipsMetal:.2f}\nO valor Total é R$ {valorTotal:.2f}')
