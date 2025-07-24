import json
import datetime
import random
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

##############################################################################
# Funções auxiliares para criar texto em degradê em um Canvas
##############################################################################


def hex_to_rgb(hex_color):
    """Converte uma cor em formato hexadecimal (#RRGGBB) em tupla (R, G, B)."""
    hex_color = hex_color.lstrip('#')
    return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))


def rgb_to_hex(rgb):
    """Converte uma tupla (R, G, B) em cor hexadecimal (#RRGGBB)."""
    return '#{:02x}{:02x}{:02x}'.format(*rgb)


def interpolate_color(color1, color2, t):
    """
    Faz interpolação linear entre duas cores (R, G, B).
    t varia de 0.0 a 1.0, sendo 0 => color1 e 1 => color2.
    """
    r1, g1, b1 = color1
    r2, g2, b2 = color2
    r = int(r1 + (r2 - r1) * t)
    g = int(g1 + (g2 - g1) * t)
    b = int(b1 + (b2 - b1) * t)
    return (r, g, b)


def create_gradient_text(canvas, x, y, text, start_hex, end_hex, font=("Helvetica", 28, "bold")):
    """
    Desenha um texto caractere a caractere no Canvas,
    criando um degradê de cor entre start_hex e end_hex.
    """
    start_rgb = hex_to_rgb(start_hex)
    end_rgb = hex_to_rgb(end_hex)
    length = len(text)
    offset_x = 0  # deslocamento horizontal para cada caractere

    for i, char in enumerate(text):
        if length > 1:
            t = i / (length - 1)
        else:
            t = 0
        color_rgb = interpolate_color(start_rgb, end_rgb, t)
        color_hex = rgb_to_hex(color_rgb)

        c = canvas.create_text(
            x + offset_x,
            y,
            text=char,
            fill=color_hex,
            font=font,
            anchor="nw"
        )
        bbox = canvas.bbox(c)
        char_width = bbox[2] - bbox[0] if bbox else 20
        offset_x += char_width

##############################################################################
# Funções para desenhar um fundo "futurista" com borda neon
##############################################################################


def draw_futuristic_background(canvas, width, height):
    """
    Desenha um retângulo de borda neon e algumas linhas decorativas no Canvas.
    """
    # Limpa qualquer desenho anterior
    canvas.delete("all")

    # Cor de neon
    neon_color = "#00ffff"
    # Desenha um retângulo com borda neon
    border_width = 3
    margin = 10
    canvas.create_rectangle(
        margin, margin,
        width - margin, height - margin,
        outline=neon_color,
        width=border_width
    )

    # Desenha algumas linhas "abstratas" como efeito decorativo
    # Aqui você pode personalizar quantas quiser, posições, etc.
    for i in range(10):
        x1 = random.randint(margin, width - margin)
        y1 = random.randint(margin, height - margin)
        x2 = random.randint(margin, width - margin)
        y2 = random.randint(margin, height - margin)
        canvas.create_line(x1, y1, x2, y2, fill=neon_color, width=1)

    # Adiciona um leve "glow" desenhando retângulos concêntricos
    # com cores gradualmente mais escuras
    for glow in range(1, 5):
        offset = margin + glow*4
        alpha = 255 - glow*40  # diminui a intensidade da cor
        # Garante que não fique negativo
        alpha = max(alpha, 0)
        glow_color = f"#{alpha:02x}ffff"  # mexendo apenas no canal R
        canvas.create_rectangle(
            offset, offset,
            width - offset, height - offset,
            outline=glow_color,
            width=1
        )

##############################################################################
# Lógica dos desafios
##############################################################################


try:
    with open("desafios.json", "r", encoding="utf-8") as file:
        desafios = json.load(file)
except FileNotFoundError:
    desafios = [
        {"categoria": "matemática", "dificuldade": 1,
         "enunciado": "2 + 2 = ?", "resposta_certa": "4"},
        {"categoria": "matemática", "dificuldade": 1,
         "enunciado": "3 + 5 = ?", "resposta_certa": "8"},
        {"categoria": "matemática", "dificuldade": 1,
         "enunciado": "10 - 4 = ?", "resposta_certa": "6"},
        {"categoria": "matemática", "dificuldade": 1,
         "enunciado": "6 / 2 = ?", "resposta_certa": "3"},
        {"categoria": "fundamentos", "dificuldade": 1,
         "enunciado": "Faça um programa que leia o nome e duas notas de um aluno, calcule a média e exiba o resultado.",
         "resposta_certa": "nome = input('Nome: ')\nnota1 = float(input('Nota 1: '))\nnota2 = float(input('Nota 2: '))\nprint((nota1+nota2)/2)"}
    ]

desempenho = {"acertos": 0, "erros": 0,
              "porcentagem_acertos": 0, "desempenho_dia": {}}
ultima_data_desafio = None


def gerar_desafio(dificuldade, data_atual):
    desafios_filtrados = [
        d for d in desafios if d["dificuldade"] == dificuldade]
    return random.choice(desafios_filtrados) if desafios_filtrados else None


def analisar_desempenho(respostas, data_atual):
    global desempenho
    acertos = [r for r in respostas if r["acertou"]]
    desempenho["acertos"] = len(acertos)
    desempenho["erros"] = len(respostas) - len(acertos)
    if respostas:
        desempenho["porcentagem_acertos"] = (
            len(acertos) / len(respostas)) * 100
    else:
        desempenho["porcentagem_acertos"] = 0
    desempenho["desempenho_dia"][str(data_atual)] = desempenho["acertos"]


def fornecer_feedback(resposta, desafio):
    if resposta.strip() == desafio["resposta_certa"].strip():
        return "Parabéns! Você acertou!"
    return "Não foi dessa vez. A resposta certa é:\n" + desafio["resposta_certa"]


def enviar_resposta():
    global ultima_data_desafio
    resposta = resposta_entry.get()
    if desafios:
        desafio_atual = desafios[0]
    else:
        desafio_atual = gerar_desafio(1, datetime.date.today())
        if not desafio_atual:
            messagebox.showinfo(
                "Feedback", "Parabéns! Você completou todos os desafios!")
            return

    feedback = fornecer_feedback(resposta, desafio_atual)
    messagebox.showinfo("Feedback", feedback)

    analisar_desempenho([{"acertou": resposta.strip()
                          == desafio_atual["resposta_certa"].strip()}],
                        datetime.date.today())
    desafios.pop(0)

    if desafios:
        novo_desafio = desafios[0]
        desafio_var.set(novo_desafio["enunciado"])
    else:
        novo_desafio = gerar_desafio(1, datetime.date.today())
        if novo_desafio:
            desafio_var.set(novo_desafio["enunciado"])
        else:
            desafio_var.set("Parabéns! Você completou todos os desafios!")

    resposta_entry.delete(0, tk.END)

##############################################################################
# Interface principal
##############################################################################


root = tk.Tk()
root.title("Desafios de Programação Python")
root.geometry("800x600")
root.configure(bg="#0f0f0f")

# Canvas de fundo para desenhar o visual "futurista"
background_canvas = tk.Canvas(root, bg="#0f0f0f", highlightthickness=0)
background_canvas.pack(fill="both", expand=True)

# Ao redimensionar a janela, redesenha o fundo


def on_resize(event):
    width = event.width
    height = event.height
    draw_futuristic_background(background_canvas, width, height)


background_canvas.bind("<Configure>", on_resize)

# Frame que vai conter o conteúdo, posicionado ao centro
content_frame = ttk.Frame(root, style="TFrame")
content_frame.place(relx=0.5, rely=0.5, anchor="center")

# Configurações de estilo
style = ttk.Style()
style.theme_use("clam")

style.configure("TFrame", background="#0f0f0f")
style.configure("TLabel",
                background="#0f0f0f",
                foreground="#ffffff",
                font=("Helvetica", 12))
style.configure("TButton",
                background="#303030",
                foreground="#00ffff",
                font=("Helvetica", 11, "bold"),
                padding=6)
style.map("TButton",
          background=[('active', '#505050')],
          foreground=[('active', '#00ff99')])
style.configure("TEntry",
                fieldbackground="#303030",
                foreground="#ffffff",
                bordercolor="#00ff99",
                font=("Helvetica", 12))

# Ajusta colunas e linhas para centralizar
content_frame.columnconfigure(0, weight=1)
for r in range(5):
    content_frame.rowconfigure(r, weight=0)

# Canvas para desenhar o título com degradê
title_canvas = tk.Canvas(content_frame, width=700, height=80,
                         bg="#0f0f0f", highlightthickness=0)
title_canvas.grid(column=0, row=0, pady=(0, 20))

# Desenha o texto do título com degradê (do azul #00ffff ao verde #00ff99)
create_gradient_text(
    title_canvas,
    x=10,
    y=10,
    text="Desafios de Programação",
    start_hex="#00ffff",
    end_hex="#00ff99",
    font=("Helvetica", 36, "bold")
)

desafio_var = tk.StringVar()
data_atual = datetime.date.today()
desafio_inicial = gerar_desafio(1, data_atual)
if desafio_inicial:
    desafio_var.set(desafio_inicial["enunciado"])
else:
    desafio_var.set("Nenhum desafio disponível.")

# Label do desafio
desafio_label = ttk.Label(
    content_frame, textvariable=desafio_var, wraplength=700, font=("Helvetica", 14)
)
desafio_label.grid(column=0, row=1, pady=10, sticky="n")

# Entrada de texto para resposta (mais alta usando ipady)
resposta_entry = ttk.Entry(content_frame, width=70)
resposta_entry.grid(column=0, row=2, padx=10,
                    pady=(10, 10), sticky="ew", ipady=10)
resposta_entry.focus()

# Botão Enviar (abaixo da caixa de entrada)
enviar_button = ttk.Button(
    content_frame, text="Enviar Resposta", command=enviar_resposta
)
enviar_button.grid(column=0, row=3, pady=10)

# Label de desempenho
desempenho_var = tk.StringVar(value="Desempenho: 0%")
desempenho_label = ttk.Label(
    content_frame, textvariable=desempenho_var, font=("Helvetica", 14)
)
desempenho_label.grid(column=0, row=4, pady=10)


def atualizar_desempenho():
    desempenho_var.set(f"Desempenho: {desempenho['porcentagem_acertos']:.2f}%")
    root.after(1000, atualizar_desempenho)


atualizar_desempenho()

root.mainloop()
