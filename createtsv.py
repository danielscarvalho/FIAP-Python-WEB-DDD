# create tsv
import random
import math

print("Criando arquvivo tsv")

f = open("dados1.tsv","w")

for linha in range(1000):
    random_float = random.random()*1000
    random_integer = random.randint(200,999)
    seno = math.sin(math.radians(linha))

    if linha % 2 == 0: #Verificando se o valor é par
        val = math.sqrt(random_integer)
    else:
        val = random_integer * -1
    
    output = f"A\t{linha}\t{(linha+1)*100}\t{random_integer}\t{random_float}\t{seno}\t{val}\n"
    
    f.write(output)

f.close() #Salvar o arquivo...