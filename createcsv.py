# create csv
import random
import math

print("Criando arquvivo CSV")

f = open("dados1.csv","w")

for linha in range(1000):
    random_float = random.random()*1000
    random_integer = random.randint(200,999)
    seno = math.sin(math.radians(linha))

    if linha % 2 == 0: #Verificando se o valor é par
        val = math.sqrt(random_integer)
    else:
        val = random_integer * -1
    
    output = f"A;{linha};{(linha+1)*100};{random_integer};{random_float};{seno};{val}\n"
    
    f.write(output)

f.close() #Salvar o arquivo...