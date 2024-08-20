from tkinter import *
from tkinter import ttk
from functions import registrar_voto, encerrar_votacao

root = Tk()
root.title("Urna Eletrônica")
root.geometry("300x200")

candidatos = {1: "João Silva", 2: "Carlos Andrade"}
list_votos = []

label_instrucoes = Label(root, text="Escolha seu candidato:")
label_instrucoes.grid(column=0, row=0, padx=10, pady=10)

button_joao = Button(root, text="João Silva (1)", command=lambda: registrar_voto(1, list_votos, candidatos, label_status))
button_joao.grid(column=0, row=1, padx=10, pady=10)

button_carlos = Button(root, text="Carlos Andrade (2)", command=lambda: registrar_voto(2, list_votos, candidatos, label_status))
button_carlos.grid(column=0, row=2, padx=10, pady=10)

button_encerrar = Button(root, text="Encerrar Votação", command=lambda: encerrar_votacao(list_votos, label_status))
button_encerrar.grid(column=0, row=3, padx=10, pady=10)

label_status = Label(root, text="")
label_status.grid(column=0, row=4, padx=10, pady=10)

root.mainloop()
