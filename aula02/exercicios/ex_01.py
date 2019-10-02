
import requests
import random 
URL = 'http://localhost:5000/soma'

PAYLOAD = {
    'numeros': [ random.randint(0,9) for x in range(10)]


}

res = requests.post(URL, json=PAYLOAD)

if res.status_code == 200:
    print('Soma = {} '.format(
        res.json().get('soma'))
    )
else:
    print(res.text)
