import requests

def buscar_cep():
    request = requests.get("http://viacep.com.br/ws/01001000/json/")
    print(request.content)

buscar_cep()