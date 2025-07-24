tamanho = input('Escolha o tamano do pote de açaí (P,M,G): ')
print('COBETURAS:\nLeite ninha\nLeite condensado\nAmendoim\nCereja')
cob_leite_po = input('Acrescentar Leite Ninho (s/n): ')
cob_Leite_cond = input('Acrescentar Leite condensado (s/n): ')
cob_amendoim = input('Acrescentar Amendoim (s/n): ')
cob_cereja = input('Acrescentar Cereja (s/n): ')

valor = float()

if tamanho:
    if tamanho == 'p':
        valor += 10
    elif tamanho == 'm':
        valor += 15
    else:
        valor += 20

if cob_leite_po == 's':
    valor += 2
if cob_Leite_cond == 's':
    valor += 1.5
if cob_amendoim == 's':
    valor += 2.3
if cob_cereja == 's':
    valor += 3
print(f"\nValor Total: R$ {valor:.2f}")
