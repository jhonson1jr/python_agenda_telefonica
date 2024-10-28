from ctypes import windll
from tkinter.ttk import *
from tkinter import *
from tkinter import messagebox
from tkinter import ttk

# Permite a entrada se o tamanho atual for menor que 20 caracteres
def limitar_entrada(char, texto_atual):
    return len(texto_atual) < 20

# ------ Cores ------ #
cor_preto = "#000000" # Preto
cor_cinza = "#F0F3F5" # cinza
cor_branco = "#FEFFFF" # branco
cor_azul_claro = "#31a8d0" # azul claro
cor_marrom_claro = "#403D3D" # letra
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
label_nome = Label(frame_centro, text="Nome*:", anchor=NW, font=('Ivy 10'), bg=cor_cinza, fg=cor_marrom_claro)
label_nome.place(x=10, y=20)
# os Entry só aceitarão até 20 caracteres
input_nome = Entry(frame_centro, width=25, justify="left", font=('', 10), highlightthickness=1, validate='key', relief=FLAT, validatecommand=valida_qtde_caracteres)
input_nome.place(x=80, y=20)

label_sexo = Label(frame_centro, text="Sexo*:", anchor=NW, font=('Ivy 10'), bg=cor_cinza, fg=cor_marrom_claro)
label_sexo.place(x=10, y=45)
combo_sexo = Combobox(frame_centro, width=27)
combo_sexo['value'] = ('', 'F', 'M')
combo_sexo.place(x=80, y=45)

label_telefone = Label(frame_centro, text="Telefone*:", anchor=NW, font=('Ivy 10'), bg=cor_cinza, fg=cor_marrom_claro)
label_telefone.place(x=10, y=70)
input_telefone = Entry(frame_centro, width=25, justify="left", font=('', 10), highlightthickness=1, validate='key', relief=FLAT, validatecommand=valida_qtde_caracteres)
input_telefone.place(x=80, y=70)

label_email = Label(frame_centro, text="E-mail*:", anchor=NW, font=('Ivy 10'), bg=cor_cinza, fg=cor_marrom_claro)
label_email.place(x=10, y=95)
input_email = Entry(frame_centro, width=25, justify="left", font=('', 10), highlightthickness=1, validate='key', relief=FLAT, validatecommand=valida_qtde_caracteres)
input_email.place(x=80, y=95)

btn_buscar = Button(frame_centro, text="Buscar", font=('Ivy 8 bold'), bg=cor_cinza, fg=cor_marrom_claro, relief=RAISED, overrelief=RIDGE)
btn_buscar.place(x=285, y=20)
input_buscar = Entry(frame_centro, width=20, justify="left", font=('', 10), highlightthickness=1, validate='key', validatecommand=valida_qtde_caracteres)
input_buscar.place(x=340, y=21)

btn_listar = Button(frame_centro, text="Listar todos", font=('Ivy 8 bold'), bg=cor_azul_claro, fg=cor_marrom_claro, relief=RAISED, overrelief=RIDGE)
btn_listar.place(x=285, y=55)

btn_salvar = Button(frame_centro, text="Adicionar", width=10, font=('Ivy 8 bold'), bg=cor_verde, fg=cor_marrom_claro, relief=RAISED, overrelief=RIDGE)
btn_salvar.place(x=400, y=55)

btn_atualizar = Button(frame_centro, text="Atualizar", width=10,  font=('Ivy 8 bold'), bg=cor_cinza, fg=cor_marrom_claro, relief=RAISED, overrelief=RIDGE)
btn_atualizar.place(x=400, y=85)

btn_excluir = Button(frame_centro, text="Excluir", width=10, font=('Ivy 8 bold'), bg=cor_vermelho, fg=cor_marrom_claro, relief=RAISED, overrelief=RIDGE)
btn_excluir.place(x=400, y=115)

# ------ Configurando a Tabela de Listagem ------ #
dados_cabecalho = ['Nome', 'Sexo', 'Telefone', 'E-mail']
dados_tabela = [
    ['Joao', 'M', '13997426655', 'joao@email.com'],
    ['Joana', 'F', '1134562200', 'joana@email.com'],
]

tabela = ttk.Treeview(frame_tabela, selectmode="extended", columns=dados_cabecalho, show="headings")

# barra de rolagem vertical e horizontal:
barra_vertical   = ttk.Scrollbar(frame_tabela, orient="vertical", command=tabela.yview)
barra_horizontal = ttk.Scrollbar(frame_tabela, orient="horizontal", command=tabela.xview)

tabela.configure(yscrollcommand=barra_vertical.set, xscrollcommand=barra_horizontal.set)

tabela.grid(column=0, row=0, sticky='nsew')
barra_vertical.grid(column=1, row=0, sticky='ns')
barra_horizontal.grid(column=0, row=1, sticky='ew')

# cabecalho tabela:
tabela.heading(0, text='Nome', anchor='nw')
tabela.heading(1, text='Sexo', anchor='nw')
tabela.heading(2, text='Telefone', anchor='nw')
tabela.heading(3, text='E-mail', anchor='nw')

# corpo tabela:
tabela.column(0, width=170, anchor='nw')
tabela.column(1, width=40, anchor='nw')
tabela.column(2, width=100, anchor='nw')
tabela.column(3, width=150, anchor='nw')

for item in dados_tabela:
    tabela.insert('', 'end', values=item)

janela.mainloop()

