import csv
def ler_dados_csv(caminho_arquivo)
    dados = []

    with open(caminho_arquivo, mode 'r', encoding 'utf-8') as arquivo_csv:   #para abir o arquivo em modo leitura conforme a codificação utf-8
         leitor_csv = csv.DictReader(arquivo_csv)   # para criar um leitor do CSV que vai mapeia os cabeçalhos para as chaves do dicionário
         for linha in leitor_cvs    # para representar cada linha do arquivo que eu quero
         dados.append(dict(linha))  # para adicionar uma linha do dicionário na lista

return dados

