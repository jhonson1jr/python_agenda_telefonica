# arquivo de manipulação do CSV
import csv

# funcao para adicionar dados no arquivo CSV
def salvarDados(dados):
    # acessando o CSV (a = append):
    with open('dados.csv', 'a+', newline='') as arquivo:
        escrever = csv.writer(arquivo)
        escrever.writerow(dados)

# funcao para sobrescrever o arquivo CSV:
def salvarArrayDados(dados):
    # acessando o CSV (w = write):
    with open('dados.csv', 'w', newline='') as arquivo:
        escrever = csv.writer(arquivo)
        escrever.writerows(dados)

# funcao para ler dados do arquivo CSV:
def verDados():
    dados = []
    with open('dados.csv') as arquivo:
        arquivo_csv = csv.reader(arquivo)
        for linha in arquivo_csv:
            dados.append(linha)
    return dados

# funcao para remover algum registro usando o campo telefone como campo chave
def removerDados(telefone):
    nova_lista = []
    with open('dados.csv', 'r') as arquivo:
        arquivo_csv = csv.reader(arquivo)
        for linha in arquivo_csv:
            nova_lista.append(linha)
            for campo in linha: # iterando campo a campo a cada iteração de linha
                if campo == telefone:
                    nova_lista.remove(linha) # se o campo da repetição for igual ao telefone informado por parametro, remove

    #após processar os dados do arquivo, salva o novo array com os registros atualizados:
    salvarArrayDados(nova_lista)

# funcao para atualizar os dados do CSV usando telefone como parametro
def atualizarDados(telefone, novos_dados):
    nova_lista = []
    with open('dados.csv', 'r') as arquivo:
        arquivo_csv = csv.reader(arquivo)
        for linha in arquivo_csv:
            nova_lista.append(linha)
            for campo in linha: # iterando campo a campo a cada iteração de linha
                if campo == telefone: # se o campo da repetição for igual ao telefone informado:
                    nome  = novos_dados[0]
                    sexo  = novos_dados[1]
                    tel   = novos_dados[2]
                    email = novos_dados[3]

                    dados_atualizados = [nome, sexo, tel, email]

                    # pegando o indice da linha para usar de referencia na sobrescrita dos dados:
                    index_linha = nova_lista.index(linha)
                    nova_lista[index_linha] = dados_atualizados
    salvarArrayDados(nova_lista)


# funcao para ler pesquisar do arquivo CSV:
def pesquisarDados(texto):
    dados = []
    with open('dados.csv') as arquivo:
        arquivo_csv = csv.reader(arquivo)
        for linha in arquivo_csv:
            for campo in linha:
                if campo == texto: # se o texto pesquisado for corresponder a algum registro:
                    dados.append(linha)
    return dados