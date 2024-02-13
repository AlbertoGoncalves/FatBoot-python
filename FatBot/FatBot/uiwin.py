import tkinter as tk
from tkinter import ttk
from FatBot.excelPandasJson import automacao

def win():
    window = tk.Tk()
    window.title('AutoBoot')
    # window.geometry('500x500')
    ttk.Label(window, text="Selecione abaixo qual tipo de boot deseja iniciar",
              background='green', foreground="white",
              font=("Times New Roman", 15)).grid(column=0, row=1, pady= 5, padx= 5)

    ttk.Label(window, text="Automações :",
              font=("Times New Roman", 15)).grid(column=0, row=6, padx=25)
    n = tk.StringVar()

    # Conteudo opc (1 - Incluir SC) (2 - Teams) (3 - Enviar E-Mails)
    monthchoosen = ttk.Combobox(window, width=27, textvariable=n)
    monthchoosen['values'] = ('Incluir SC',
                              'Msg Teams',
                              'Enviar E-Mail',
                              'E-mail Protocolo Compras',
                              'Teste paginas Chrome')
    monthchoosen.grid(column=0, row=7)

    botao = ttk.Button(window, text="Iniciar automação", command=lambda: automacao(monthchoosen.current()))
    botao.grid(column=0, row=9, pady=10)

    window.mainloop()
