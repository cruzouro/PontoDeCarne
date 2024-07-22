import tkinter as tk

def verificar_temperatura():
    # Limpa o rótulo de resultado antes de exibir o novo resultado
    resultado_label.config(text="")
    
    try:
        point = int(entry.get())
    except ValueError:
        resultado_label.config(text="Temperatura inválida", fg="Snow")
    else:
        if 48 <= point <= 53:
            resultado = "Mal Passado"
        elif 54 <= point <= 59:
            resultado = "Ao ponto para mal passado"
        elif 60 <= point <= 64:
            resultado = "Ao ponto"
        elif 65 <= point <= 69:
            resultado = "Ao Ponto para bem passado"
        elif 70 <= point <= 79:
            resultado = "Bem passado"
        elif point >= 80:
            resultado = "Passado"
        elif point <= 47:
            resultado = "A carne está Crua"
        
        resultado_label.config(text=resultado, fg="Snow")

# Configuração da janela principal
root = tk.Tk()
root.title("Ponto da Carne")

# Configurações de cores 
bg_color = "#A0522D"  # Cor de fundo da janela
label_color = "#ffffff"  # Cor do texto do rótulo
button_bg_color = "#8B4513"  # Cor de fundo do botão
button_fg_color = "#ffffff"  # Cor do texto do botão

# Configura a cor de fundo da janela
root.configure(bg=bg_color)

# Rótulo
label = tk.Label(root, text="  Insira a temperatura da carne em ºC:  ", bg=bg_color, fg=label_color, font=("Helvetica", 12))
label.pack(pady=10)

# Campo de entrada
entry = tk.Entry(root)
entry.pack(pady=5)

# Botão para verificar a temperatura
button = tk.Button(root, text="Verificar", command=verificar_temperatura, bg=button_bg_color, fg=button_fg_color, font=("Helvetica", 12))
button.pack(pady=20)

# Rótulo para exibir o resultado
resultado_label = tk.Label(root, text="", bg=bg_color, font=("Helvetica", 12))
resultado_label.pack(pady=10)

# Loop principal da aplicação
root.mainloop()
