# Apendendo Python com um RPG de Texto.
# onde o jogador pode escolher o Nome seu personagem.

# Nome do Jogador

print("Bem-vindo ao RPG de Texto!")
nomeJogador = input('Digite o nome do seu personagem: ')

print(
    f'\nOlá, {nomeJogador}! Você está prestes a embarcar em uma aventura épica!\n')
# Dicionario para armazenar os atributos do Jogador
jogador = {
    'nome': nomeJogador,
    'raça': 'Humano',
    'classe': 'mago',
    'atributos': {
        'força': 10,
        'destreza': 8,
        'inteligência': 6
    },
    'vida': 100,  # Vida inicial do Jogador
    'habilidades': {
        'ataque': 5,
        'defesa': 3
    }
}
# Exibindo as informações do Jogador


def informacoes_jogador(jogador):
    print('--' * 30)

    print("\nEstatísticas do Jogador:\n")
    print(f"Nome: {jogador['nome']}")
    print(f"Raça: {jogador['raça']}")
    print(f"Classe: {jogador['classe']}")
    print(f"Vida: {jogador['vida']}\n")

    print('--' * 30)

    # Atributos do Jogador
    print("\nAtributos:\n")

    print(f"Força: {jogador['atributos']['força']}")
    print(f"Destreza: {jogador['atributos']['destreza']}")
    print(f"Inteligência: {jogador['atributos']['inteligência']}\n")

    print('--' * 30)

    # Habilidades do Jogador
    print("Habilidades:")

    print(f"Ataque: {jogador['habilidades']['ataque']}")
    print(f"Defesa: {jogador['habilidades']['defesa']}\n")


informacoes_jogador(jogador)

# Aprendendo listas em Python
# Atributos do Jogador
# Invemtário do Jogador

inventario = []


def adicionar_item(inventario, item):
    if item not in inventario:
        inventario.append(item)
        print(f"\nVocê adicionou '{item}' ao seu inventário.")
    else:
        print(f"\n'{item}' já está no seu inventário.")


def mastrar_inventario(inventario):
    if inventario:
        print("\nSeu inventário contém:")
        for item in inventario:
            print(f"- {item}")
    else:
        print("\nSeu inventário está vazio.")


print("\nSeu inventário está vazio por enquanto.")
print("\nVocê pode coletar itens durante sua aventura.")
print(f"\nVamos começar sua jornada {nomeJogador}!")
print("\nVocê acorda em uma floresta densa e escura, cercado por árvores altas.")
print("\nÀ sua frente, há uma 'Tocha desgastada'. Adicione-a ao seu inventário? (sim/não)")

resposta = input().lower()
if resposta == 'sim':
    adicionar_item(inventario, 'Tocha desgastada')
else:
    adicionar_item(inventario)

mastrar_inventario(inventario)

if 'Tocha desgastada' in inventario:
    print("\nVocê acende a Tocha desgastada e ilumina o caminho à sua frente.")
else:
    print("\nVocê está no escuro e não consegue ver o que está à sua frente.")
