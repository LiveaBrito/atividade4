'''Exercicio 2: Crie um programa que gera um perfil de usuário aleatório
 usando a API 'Random User Generator'.
O programa deve exibir o nome, email e país do usuário gerado.'''

import requests

#Abaixo faz a requisição à API Random User Generator
response = requests.get("https://randomuser.me/api/")

#Verificando se a requisição foi bem sucedida
if response.status_code == 200:
    dados = response.json()
    usuario = dados['results'][0]
    
    nome = f"{usuario['name']['first']} {usuario['name']['last']}"
    email = usuario['email']
    pais = usuario['location']['country']
    
    print("Perfil do Usuário Gerado Aleatoriamente")
    print(f"Nome: {nome}")
    print(f"Email: {email}")
    print(f"País: {pais}")
else:
    print(f"Erro ao acessar a API. Código: {response.status_code}")

    
