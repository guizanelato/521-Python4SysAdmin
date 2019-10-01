import requests


cep = input("Digite o seu CEP: ") 

URL = 'https://viacep.com.br/ws/{}/json/'.format(cep)
response = requests.get(URL)


if response.status_code == 200:
    #logradouro = response.json().get('logradouro')
    #logradouro = response.json()['logradouro']
    dic = response.json()
    print("Endereço:", dic["logradouro"])
else:
    print(response.text)
    
    
    
