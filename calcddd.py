# Implementar solução para um algoritmo da sua escolha em:
# LAB: https://projecteuler.net/ Projeto individual, escolher um desafio do Project Euler

def calc(a, b):
    return a**b

x = float(input("Informe valor de x: "))
y = float(input("Informe valor de y: "))

resultado = calc(x, y)

print(f"x = {x} e y = {y} resultado = {resultado}")