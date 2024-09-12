# Ler arquivo .csv e exibir estatísticas por coluna, feature ou campo

# Ler linha a linha
# Separar a linha de cabeçalho
# Converter todo os campos para numérico
# Carregar os dados numéricos em uma lista para uso
# Calcular elementos estatísticos

import statistics as s

arquivo = open("diabetes.csv","r")

lista = []
cabeçalho = arquivo.readline().split(",")

for linha in arquivo:
    lista.append(linha.split(","))

print(cabeçalho)
print(len(lista)[0])

arquivo.close()