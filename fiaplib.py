# FIAP LIB
import statistics

def primeiro (lista):
    """Retorna o primeiro elemento de uma lista, tupla ou string"""
    return lista[0]

def último (lista):
    """Retorna o último elemento de uma lista, tupla ou string"""
    return lista[-1]

def média (lista):
    """Retorna a média de uma lista ou tupla de inteiros ou floats"""
    return sum(lista)/len(lista)

def estatística(lista):
    """Retorna estatísticas sobre a lista em um dicionário"""
    saída = { "mean": statistics.mean(lista),
              "stev": statistics.stdev(lista),
              "max": max(lista),
              "min": min(lista),
              "size": len(lista),
              "mode": statistics.mode(lista)
             } # dict
    
    return saída