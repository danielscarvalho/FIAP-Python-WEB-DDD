# Daniel - 26/08/24 - FIAP - WEB - Python
# Obter números do usuário e acumular
# em uma lista
# Exibir dados da lista, informações estatísticas 
# de soma, max, min, etc...

import statistics as stats

lista = []
status = True

while(status):
    entrada = input("Entrar com valor float ou inteiro: ")

    if entrada == "":
        status = False
    else:
        lista.append(float(entrada))

print(len(lista), max(lista), min(lista), stats.mean(lista), stats.mode(lista))

