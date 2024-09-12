# Pegar texto do teclado e salvar em arquivo texto
# Se o arquvo existir, append, se não criar arquivo novo
# Linha vazia finaliza o processamento e fecha (salva) o arquivo

nome_arquivo = input("Digite o nome do arquivo: ")

arquivo = open(nome_arquivo, "a") # a - append

continuar = True

while(continuar): #Loop infinito do prompt...
    texto = input("👉🏻 ")

    if texto == "":
        continuar = False
    else:
        arquivo.write(texto + "\n")

arquivo.close() # salvar arquivo