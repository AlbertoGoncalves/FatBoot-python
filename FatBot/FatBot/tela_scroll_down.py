import tkinter as tk
from tkinter import ttk
from tkinter import messagebox, Tk, Label, Entry, Button

from botcity.base.utils import find_bot_class
import FatBot.bot1

klass = find_bot_class(FatBot.bot1)[0]


def automacao1(opc, opc1):
    klass.main(opc, opc1)

def win():
    window = Tk()
    window.title('AutoBoot')
    # window.geometry('400x250')
    # ttk.Label(window, text="Selecione abaixo qual tipo de boot deseja iniciar",
    #           background='green', foreground="white",
    #           font=("Times New Roman", 15)).grid(column=0, row=1, pady= 5, padx= 5)

    timeWait_label = Label(window,text="Tempo de rolagem", font=("Times New Roman", 15))
    timeWait_label.grid(column=0, row=0, pady=10, padx=10)

    timeWait_entry = Entry(width=15)
    timeWait_entry.grid(column=0, row=1, columnspan=1)


    numScrollDown = Label(window, text="Nº rolagem para baixo", font=("Times New Roman", 15))
    numScrollDown.grid(column=2, row=0, pady=10, padx=10)

    numScrollDown_entry = Entry(width=15)
    numScrollDown_entry.grid(column=2, row=1, columnspan=1)


    botao = ttk.Button(window, text="Iniciar automação", command=lambda: automacao1(timeWait_entry.get(),numScrollDown_entry.get()))
    botao.grid(column=0, row=9, pady=10)

    window.mainloop()




