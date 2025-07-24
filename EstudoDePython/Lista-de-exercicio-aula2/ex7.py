tpc = input('Digite qual o tipo de consumidor ("R") para Residencial, ("I") para Industrial e ("C") para Comercial: ')

consAgua = float(input('Digite o seu consumo de agua por m³: '))

if tpc == 'R' or tpc == 'r':
    gasto = 5 + 0.05 * consAgua

elif tpc == 'C' or tpc == 'c':
    if consAgua <= 80:
        gasto = 500
    else:
        gasto = 500 + 0.25 * (consAgua - 80)
elif tpc == 'I' or tpc == 'i':
    if consAgua <= 100:
        gasto = 800
    else:
        gasto = 800 + 0.04 * (consAgua - 100)
print(f'O valor da conta de água é R$ {gasto:.2f}')
