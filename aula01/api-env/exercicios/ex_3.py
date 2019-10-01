import requests 


email = input("Digite o seu e-mail: ")

URL = 'https://gen-net.herokuapp.com/api/users'

response = requests.get(URL, params={
    'email': email
})

# https://gen-net.herokuapp.com/api/users?email=guilherme.zanelato@gmail.com <- no postman

if response.status_code == 200:
    print(response.json())
else:
    print(response.text)
    
