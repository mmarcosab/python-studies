import requests
import json

def buscar_cep():
    request = requests.get("http://viacep.com.br/ws/01001000/json/")
    print(request.content)
    all_fields = json.loads(request.content)
    print(all_fields)
    print(all_fields[0]['cep'])

if __name__ == '__main__':
    buscar_cep()