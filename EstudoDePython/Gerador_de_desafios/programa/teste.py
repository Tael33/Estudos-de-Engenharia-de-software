import json
import datetime
import random
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

# Funções auxiliares para degradê


def hex_to_rgb(hex_color):
    hex_color = hex_color.lstrip('#')
    return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))


def rgb_to_hex(rgb):
    return '#{:02x}{:02x}{:02x}'.format(*rgb)


def interpolate_color(color1, color2, t):
    r1, g1, b1 = color1
    r2, g2, b2 = color2
    return (int(r1 + (r2 - r1) * t), int(g1 + (g2 - g1) * t), int(b1 + (b2 - b1) * t))


def create_gradient_text(canvas, x, y, text, start_hex, end_hex, font=("Helvetica", 24, "bold")):
    start_rgb = hex_to_rgb(start_hex)
    end_rgb = hex_to_rgb(end_hex)
    length = len(text)
    offset_x = 0

    for i, char in enumerate(text):
        t = i / (length - 1) if length > 1 else 0
        color_hex = rgb_to_hex(interpolate_color(start_rgb, end_rgb, t))
        c = canvas.create_text(x + offset_x, y, text=char,
                               fill=color_hex, font=font, anchor="nw")
        bbox = canvas.bbox(c)
        offset_x += (bbox[2] - bbox[0]) if bbox else 15


# Configuração da interface
root = tk.Tk()
root.title("Desafios Futuristas")
root.geometry("800x500")
root.configure(bg="#0f0f0f")

# Frame principal com bordas arredondadas
main_frame = tk.Frame(root, bg="#191919", bd=2, relief="ridge")
main_frame.place(relx=0.5, rely=0.5, anchor="center", width=600, height=350)

# Canvas para o título
title_canvas = tk.Canvas(main_frame, width=500, height=50,
                         bg="#191919", highlightthickness=0)
title_canvas.pack(pady=(20, 10))
create_gradient_text(title_canvas, 10, 5, "Desafios Futuristas",
                     "#00ffff", "#00ff99", font=("Helvetica", 28, "bold"))

# Label do desafio
desafio_var = tk.StringVar(value="Resolva o desafio abaixo:")
desafio_label = tk.Label(main_frame, textvariable=desafio_var,
                         bg="#191919", fg="#ffffff", font=("Helvetica", 14))
desafio_label.pack(pady=5)

# Caixa de entrada
resposta_entry = tk.Entry(main_frame, bg="#303030", fg="#ffffff", font=(
    "Helvetica", 14), justify="center", relief="flat", bd=2)
resposta_entry.pack(pady=10, ipadx=5, ipady=5, fill="x", padx=50)

# Botão Enviar
enviar_button = tk.Button(main_frame, text="Enviar Resposta", bg="#00aa88", fg="white", font=("Helvetica", 12, "bold"),
                          relief="flat", activebackground="#008866", activeforeground="white", command=lambda: messagebox.showinfo("Resposta", "Resposta enviada!"))
enviar_button.pack(pady=10)

# Iniciar aplicação
root.mainloop()
