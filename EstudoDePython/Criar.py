import os


def criar_arquivos_py(caminho, nome_base, quantidade):
    # Verifica se o caminho existe, caso contrário, cria a pasta
    if not os.path.exists(caminho):
        os.makedirs(caminho)

    for i in range(1, quantidade + 1):
        nome_arquivo = f"{nome_base}_{i}.py"
        caminho_completo = os.path.join(caminho, nome_arquivo)

        # Cria o arquivo .py vazio
        with open(caminho_completo, 'w') as arquivo:
            arquivo.write("# Arquivo gerado automaticamente\n")

        print(f"Arquivo criado: {caminho_completo}")


# Exemplo de uso
caminho = input("Digite o caminho da pasta onde os arquivos serão criados: ")
nome_base = input("Digite o nome base dos arquivos: ")
quantidade = int(input("Digite a quantidade de arquivos a serem criados: "))

criar_arquivos_py(caminho, nome_base, quantidade)
