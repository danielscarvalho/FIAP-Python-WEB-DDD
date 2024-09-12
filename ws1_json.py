# pip3 install requests
# pip install requests

# Consumindo WEB SERVICES

import requests

URL = "https://viacep.com.br/ws/03819250/json/"

endereço = requests.get(URL).json() #JSON é um formato iqual ao do dict do Python

print(type(endereço))
print(endereço)