# -*- coding: utf-8 -*-
"""FIAP-DDD-WEBDESIGN.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1Z71StIXhZ3GeMIyjtFzIeIAZNDNfhGZt

# FIAP
## WEB DESIGN
### DDD - Python

Abientes que rodam Python:

- Console, mode interativo, python ou python3
  - python fib.py
- Console, modo inline, python -c "print(33*2/4)"
- Console online no site do Python www.python.org
- Google Colab - Ambiente notebook para ciências dos dados
- No VSCode como script, arquivo texto .py
- Python Anywhare - www.pythonanywhare.com
  - Conosole - Terminal do Linux e do Python
  - Agendar execução de programa/script Python
  - Publicar WEB API com Flasks
  - Banco de Dados MySQL (SQL)
"""

344+33

import math

math.cos(.1)

(55**2) / 2

# Fibonacci
def fib(n):
    a, b = 0, 1
    while a < n:
       print(a, end=' ')
       a, b = b, a+b
    print()

fib(1000)