import fiaplib

print("E ai galera da FIAP!!")

# Estruturas de dados: String, lista, tupla, dicionário...

l1 = [10, 20, 30, 40, 50]
f1 = [.1, .2, 2.3, .4, .5] # Lista usa []
t1 = (100, 200, 300, 5000) # Tupla é mais rápida que lista, mas é imutavel, tupla usa ()
s1 = "Vai Corinthians!!" # String é texto

l1.append(-99)

print(fiaplib.média(l1))
print(fiaplib.primeiro(l1))
print(fiaplib.último(l1))

print(fiaplib.média(t1))
print(fiaplib.primeiro(t1))
print(fiaplib.último(t1))

print(fiaplib.média(f1))
print(fiaplib.primeiro(f1))
print(fiaplib.último(f1))

print(fiaplib.primeiro(s1))
print(fiaplib.último(s1))