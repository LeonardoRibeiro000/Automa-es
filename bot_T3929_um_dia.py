#Criado por: Torre de controle
#Desenvolvido por: Leonardo Ribeiro - 13/06/2024

import pyautogui as bot
import pandas as pd
import time as tm
import tkinter as tk
from tkinter import ttk
from tkinter import simpledialog
from tkinter import messagebox

print(bot.position())
#função para capturar a data de entrada do usuário

try:
    def get_user_input():
        root = tk.Tk()
        root.withdraw()
        #capturar a entrada do usuário
        user_input = simpledialog.askstring(title="Data de Extração", prompt="Digite a data (formato dd/mm/aaaa):")
        return user_input
except KeyError:
    print(KeyError, "erro ao salvar o arquivo")
#capturar a data de entrada do usuário
data_entrada = get_user_input()

files = [
    515, 565, 566, 567, 697, 698, 699, 702, 703, 706, 717, 718, 719,
    720, 721, 722, 723, 724, 725, 732, 733, 734, 735, 736, 737, 747,
    748, 749, 753, 754, 755, 757, 758, 759, 761, 763, 764, 765, 766,
    767, 770, 771, 772, 774, 776
]

directory = "C:/Users/leona/Documents/"
dataframes = {}

for number in files:
    file_path = f"{directory}{number}.csv"
    dataframes[f'u{number}'] = pd.read_csv(file_path, sep=";", encoding='ISO-8859-1')

#base de unidades
unidade = pd.read_excel("tb_unidades 1 2 3 onda.xlsx")

print(unidade)
bot.click(x=1371, y=1037)
tm.sleep(1)
bot.click(x=156, y=186)
for bs in range(10):
    bot.press("backspace")
tm.sleep(1)
bot.write(data_entrada)
tm.sleep(2)
bot.click(x=301, y=188)
for bs in range(10):
    bot.press("backspace")
tm.sleep(1)
bot.write(data_entrada)
tm.sleep(2)
for lin in unidade.index:
    #unidades
    bot.click(x=129, y=234)
    tm.sleep(1)
    bot.write(str(unidade.loc[lin, "CD_FILIAL"]), interval=0.3)
    tm.sleep(1.5)
    bot.press("tab")
    tm.sleep(2)
    bot.click(x=335, y=572)
    tm.sleep(2)
    bot.write(str(unidade.loc[lin, "CD_FILIAL"]), interval=0.2)
    tm.sleep(2)
    bot.press("enter")
    tm.sleep(10)
    bot.press("enter")
    tm.sleep(2)

#concatenar bases
    base_concat = pd.concat([dataframes[f'u{num}'] for num in files])
    base_concat['data_extração'] = data_entrada

#salvar o arquivo
    base_concat.to_excel(f"farmacia_19_06.xlsx", index=False)
    print(f"Arquivo salvo com sucesso!!")
    
#mensagem de alerta
tk.messagebox.showinfo(title="Info", message="Tarefa realizada com sucesso!")