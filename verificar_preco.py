import csv

def obter_melhores_precos():
    with open('voos.csv', 'r') as arquivo_csv:
        leitor = csv.reader(arquivo_csv)
        cabecalho = next(leitor)  # Ignorar a linha de cabeçalho

        dados = list(leitor)

        # Ordenar os dados pelo preço (coluna index 2)
        dados_ordenados = sorted(dados, key=lambda x: float(x[2]))

        # Retornar os 15 melhores preços
        melhores_precos = dados_ordenados[:15]

        return melhores_precos

def escrever_melhores_precos():
    melhores_precos = obter_melhores_precos()

    with open('melhores_precos.csv', 'w', newline='') as arquivo_csv:
        escritor = csv.writer(arquivo_csv)
        escritor.writerow(["ID", "Source", "Price", "Currency", "Carrier", "Departure Date", "Return Date", "Stops", "Flight Numbers", "Stations", "Departure Times", "Arrival Times"])

        for preco in melhores_precos:
            escritor.writerow(preco)

# Exemplo de uso
escrever_melhores_precos()
