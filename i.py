import tkinter as tk
from tkinter import messagebox
import random

root = tk.Tk()
root.title("Juego de Adivinanza de Números")
root.geometry("300x200")

numero_secreto = random.randint(1, 100)

def verificar_adivinanza():
    try:
        adivinanza = int(entry.get())
        if adivinanza < numero_secreto:
            messagebox.showinfo("Resultado", "Demasiado bajo!")
        elif adivinanza > numero_secreto:
            messagebox.showinfo("Resultado", "Demasiado alto!")
        else:
            messagebox.showinfo("Resultado", "¡Correcto! Has adivinado el número.")
    except ValueError:
        messagebox.showerror("Error", "Por favor, introduce un número válido.")

label = tk.Label(root, text="Adivina el número (1-100):")
label.pack(pady=10)

entry = tk.Entry(root)
entry.pack(pady=5)

button = tk.Button(root, text="Verificar", command=verificar_adivinanza)
button.pack(pady=10)

root.mainloop()
