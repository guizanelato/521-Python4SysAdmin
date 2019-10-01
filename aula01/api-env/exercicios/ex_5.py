import requests

URL  = 'https://gen-net.herokuapp.com/api/users/' 

def encontrar_usuario(email):
    response = requests.get(URL, params={'email': email})
    
    if response.status_code == 200:
        r = response.json()
        return response.json()[0] if len(r) > 0 else None
    else:
        return None
    
    
def atualizar_senha(usuario, nova_senha):
    response = requests.put(URL + str(usuario.get("id")), data={
        "password": nova_senha 
        })
    
    if response.status_code == 200:
        print("Senha Atualizada com sucesso!")
    else:
        return None

email = input("Digite o seu email: ")

usuario = encontrar_usuario(email)

if not usuario:
    print("Usuário não encontrado.")
else:
        nova_senha = input("Digite sua nova senha: ")
        atualizar_senha(usuario, nova_senha)
  
