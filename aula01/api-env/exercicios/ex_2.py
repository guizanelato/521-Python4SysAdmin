import requests 

texto = input("Digite algo para ser buscado: ")

URL = "https://api.chucknorris.io/jokes/search?query={}"

response = requests.get(URL.format(texto))

if response.status_code == 200:
    for e in response.json().get('result'):
        print(e.get('value'))
else:
    print(response.text)
