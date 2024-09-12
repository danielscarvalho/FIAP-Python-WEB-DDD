# pip3 install requests
# pip install requests

# Consumindo WEB SERVICES

import requests

URL = "https://catfact.ninja/fact?max_length=300"

cat_fact = requests.get(URL).json() #JSON é um formato iqual ao do dict do Python

print(type(cat_fact))
print(cat_fact)