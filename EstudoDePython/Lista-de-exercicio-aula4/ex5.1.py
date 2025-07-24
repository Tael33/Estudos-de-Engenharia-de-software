def calcular_valor_acai():
    # Valores base do açaí de acordo com o tamanho
    valores_base = {
        'P': 10.00,
        'M': 15.00,
        'G': 20.00
    }

    # Valores das coberturas
    coberturas = {
        'Leite Ninho': 2.00,
        'Leite Condensado': 1.50,
        'Amendoim': 2.30,
        'Cereja': 3.00
    }

    print("===== CALCULADORA DE AÇAÍ =====")

    # Escolha do tamanho do pote
    while True:
        tamanho = input("Escolha o tamanho do pote (P, M ou G): ").upper()
        if tamanho in valores_base:
            break
        else:
            print("Tamanho inválido. Por favor, escolha P, M ou G.")

    # Valor inicial baseado no tamanho
    valor_total = valores_base[tamanho]

    print(f"\nValor do açaí ({tamanho}): R$ {valor_total:.2f}")
    print("\nEscolha as coberturas:")

    # Perguntar sobre cada cobertura
    for cobertura, valor in coberturas.items():
        while True:
            resposta = input(f"Acrescentar {cobertura}? (sim/não): ").lower()
            if resposta in ['sim', 'não', 'nao', 's', 'n']:
                break
            else:
                print("Resposta inválida. Por favor, responda 'sim' ou 'não'.")

        # Adicionar valor da cobertura se a resposta for sim
        if resposta in ['sim', 's']:
            valor_total += valor
            print(f"+ {cobertura}: R$ {valor:.2f}")

    # Mostrar o valor total
    print("\n===== RESUMO DO PEDIDO =====")
    print(f"Açaí tamanho {tamanho}: R$ {valores_base[tamanho]:.2f}")

    # Mostrar coberturas adicionadas
    for cobertura, valor in coberturas.items():
        if resposta in ['sim', 's']:
            print(f"{cobertura}: R$ {valor:.2f}")

    print(f"\nValor Total: R$ {valor_total:.2f}")


calcular_valor_acai()
