
import requests

payload = {
    'name':input('Digite o seu nome: '),
    'email': input('Digite o seu e-mail: '),
    'password':input('Digite a sua senha: ')
}

URL = 'https://gen-net.herokuapp.com/api/users' 

response = requests.post(URL, data = payload)

if response.status_code == 200:
    print(response.json())
else:
    print(response.text)
