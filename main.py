from tkinter.ttk import *
from tkinter import *
from tkinter import messagebox

# Permite a entrada se o tamanho atual for menor que 20 caracteres
def limitar_entrada(char, texto_atual):
    return len(texto_atual) < 20

# ------ Cores ------ #
cor_preto = "#F0F3F5" # Preto
cor_cinza = "#F0F3F5" # cinza
cor_branco = "#FEFFFF" # branco
cor_azul_claro = "#31a8d0" # azul claro
cor4 = "#403D3D" # letra
cor_azul = "#6F9FBD" # azul
cor_vermelho = "#EF5350" # vermelho
cor_verde = "#93CD95" # verde

# ------ Janela ------ #
janela = Tk()
janela.title("Agenda Telefônica")
janela.geometry("500x450")
janela.configure(background=cor_cinza)
janela.resizable(width=FALSE, height=FALSE)

style = Style(janela)
style.theme_use("clam")

# ------ Criação de um controle de validação de quantidade de caracteres digitados ------ #
valida_qtde_caracteres = (janela.register(limitar_entrada), '%S', '%P')

# ------ Frames ------ #
frame_cima = Frame(janela, width=500, height=50, bg=cor_azul_claro, relief="flat")
frame_cima.grid(row=0, column=0, pady=1, padx=0, sticky=NSEW)

frame_centro = Frame(janela, width=500, height=150, bg=cor_cinza, relief="flat")
frame_centro.grid(row=1, column=0, pady=1, padx=0, sticky=NSEW)

frame_tabela = Frame(janela, width=500, height=248, bg=cor_cinza, relief="flat")
frame_tabela.grid(row=2, column=0, pady=1, padx=10, columnspan=2, sticky=NW)

# ------ Configurando Frame_Cima ------ #
label_titulo = Label(frame_cima, text="Agenda Telefônica", anchor=NW, font=('arial 20 bold'), bg=cor_azul_claro, fg=cor_preto)
label_titulo.place(x=130, y=5)

# ------ Configurando Frame_Centro ------ #
label_nome = Label(frame_centro, text="Nome*:", anchor=NW, font=('Ivy 10'), bg=cor_cinza, fg=cor4)
label_nome.place(x=10, y=20)
# os Entry só aceitarão até 20 caracteres
input_nome = Entry(frame_centro, width=25, justify="left", font=('', 10), highlightthickness=1, validate='key', validatecommand=valida_qtde_caracteres)
input_nome.place(x=80, y=20)

janela.mainloop()

