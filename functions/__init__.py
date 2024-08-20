from tkinter import *

def contar_votos(list_votos):
    if list_votos:
        total_votos = len(list_votos)
        candidato_1 = len([votos for votos in list_votos if votos == 1])
        candidato_2 = len([votos for votos in list_votos if votos == 2])

        percent_1 = (candidato_1 / total_votos) * 100
        percent_2 = (candidato_2 / total_votos) * 100

        return percent_1, percent_2
    else:
        print("Nenhum voto foi registrado.")

def registrar_voto(numero, list_votos, candidatos, label_status):
    list_votos.append(numero)
    label_status.config(text=f"Você votou em {candidatos[numero]}.")

def encerrar_votacao(list_votos, label_status):
    percent_1, percent_2 = contar_votos(list_votos)
    if percent_1 is not None and percent_2 is not None:
        label_status.config(text=f'O resultado foi: João Silva: {percent_1:.2f}% | Carlos Andrade: {percent_2:.2f}%')
    else:
        label_status.config(text="Nenhum voto foi registrado.")
