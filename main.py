from ctypes import windll
from tkinter.ttk import *
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from dados_csv import *

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

dados_cabecalho = ['Nome', 'Sexo', 'Telefone', 'E-mail']
tabela = ttk.Treeview(frame_tabela, selectmode="extended", columns=dados_cabecalho, show="headings")

# barra de rolagem vertical e horizontal:
barra_vertical = ttk.Scrollbar(frame_tabela, orient="vertical", command=tabela.yview)
barra_horizontal = ttk.Scrollbar(frame_tabela, orient="horizontal", command=tabela.xview)

# configuração da tabela de exibição dos dados:
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


# funcao para isnerir novos dados na tabela:
def inserir():
    nome = input_nome.get()
    sexo = combo_sexo.get()
    tel = input_telefone.get()
    email = input_email.get()

    dados = [nome, sexo, tel, email]

    if validaPreenchimentoCampos(dados):        # se passar pela validação acima, salva os dados, limpa os campos e recarrega a tela:
        salvarDados(dados)
        messagebox.showinfo('Atenção!', 'Dados salvos com sucesso')
        limparCampos()
        carregarAplicacao()

# funcao para atualizar dado na tabela:
def atualizar():
    try:
        limparCampos()
        linha_tabela = tabela.focus()  # pegando a linha selecionada
        itens_tabela = tabela.item(linha_tabela)  # pegando as informações da linha no formato matriz
        dados_tabela = itens_tabela['values']  # pegando os valores(dados) da linha

        nome = dados_tabela[0]
        sexo = dados_tabela[1]
        tel_ant = str(dados_tabela[2])  # guardando o tel anterior para usar como chave na pesquisa do dado a atualizar
        email = dados_tabela[3]

        input_nome.insert(0, nome)
        combo_sexo.insert(0, sexo)
        input_telefone.insert(0, tel_ant)
        input_email.insert(0, email)

        def registrarAtualizacao():
            nome = input_nome.get()
            sexo = combo_sexo.get()
            tel = input_telefone.get()
            email = input_email.get()

            dados = [nome, sexo, tel, email]

            if validaPreenchimentoCampos(dados):
                # se passar pela validação acima, salva os dados, limpa os campos e recarrega a tela:
                atualizarDados(tel_ant, dados)
                messagebox.showinfo('Atenção!', 'Dados atualizados com sucesso')
                limparCampos()
                carregarAplicacao()

        # alterando a ação do botao salvar para processar a atualização dos dados:
        btn_salvar.configure(command=registrarAtualizacao)
    except:
        messagebox.showwarning('Atenção!', 'Selecione algum registro')

# funcao para apagar registro:
def remover():
    try:
        linha_tabela = tabela.focus()  # pegando a linha selecionada
        itens_tabela = tabela.item(linha_tabela)  # pegando as informações da linha no formato matriz
        dados_tabela = itens_tabela['values']  # pegando os valores(dados) da linha

        telefone = str(dados_tabela[2])  # guardando o tel anterior para usar como chave na pesquisa do dado a atualizar
        removerDados(telefone)
        messagebox.showinfo('Atenção!', 'Registro removido com sucesso')
        carregarAplicacao()
    except:
        messagebox.showwarning('Atenção!', 'Selecione algum registro para excluir')

# funcao para pesquisar registros:
def pesquisar():
    dados_busca = input_buscar.get()

    resultado = pesquisarDados(dados_busca)

    tabela.delete(*tabela.get_children())

    for item in resultado:
        tabela.insert('', 'end', values=item)
# ------ Configurando a Tabela de Listagem ------ #
def carregarAplicacao():
    dados_tabela = verDados() # funcao do arquivo dados_csv.py

    # limpando a tabela antes de carregar os dados (evitar duplicidade):
    tabela.delete(*tabela.get_children())

    for item in dados_tabela:
        tabela.insert('', 'end', values=item)

    # alterando a ação do botao salvar para processar salvar novos dados inicialmente:
    btn_salvar.configure(command=inserir)

# Percorrendo todas as posições do array para verificar se alguma não foi informada:
def validaPreenchimentoCampos(dados):
    preenchido = True
    for i in range(len(dados)):
        if dados[i] == '':
            messagebox.showwarning('Atenção!', 'Preencha todos os campos para atualizar')
            preenchido = False
            break
    return preenchido

# limpar os campos em tela
def limparCampos():
    input_nome.delete(0, 'end')
    combo_sexo.delete(0, 'end')
    input_telefone.delete(0, 'end')
    input_email.delete(0, 'end')
    input_buscar.delete(0, 'end')

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

btn_buscar = Button(frame_centro, text="Buscar", command=pesquisar, font=('Ivy 8 bold'), bg=cor_cinza, fg=cor_marrom_claro, relief=RAISED, overrelief=RIDGE)
btn_buscar.place(x=285, y=20)
input_buscar = Entry(frame_centro, width=20, justify="left", font=('', 10), highlightthickness=1, validate='key', validatecommand=valida_qtde_caracteres)
input_buscar.place(x=340, y=21)

btn_listar = Button(frame_centro, text="Listar todos", command=carregarAplicacao, font=('Ivy 8 bold'), bg=cor_azul_claro, fg=cor_marrom_claro, relief=RAISED, overrelief=RIDGE)
btn_listar.place(x=285, y=55)

btn_salvar = Button(frame_centro, text="Salvar", command=inserir, width=10, font=('Ivy 8 bold'), bg=cor_verde, fg=cor_marrom_claro, relief=RAISED, overrelief=RIDGE)
btn_salvar.place(x=400, y=55)

btn_atualizar = Button(frame_centro, text="Atualizar", command=atualizar, width=10,  font=('Ivy 8 bold'), bg=cor_cinza, fg=cor_marrom_claro, relief=RAISED, overrelief=RIDGE)
btn_atualizar.place(x=400, y=85)

btn_excluir = Button(frame_centro, text="Excluir", command=remover, width=10, font=('Ivy 8 bold'), bg=cor_vermelho, fg=cor_marrom_claro, relief=RAISED, overrelief=RIDGE)
btn_excluir.place(x=400, y=115)


carregarAplicacao()

janela.mainloop()

