'''Exercicio 3: Desenvolva um programa que consulte informações de endereço a partir de um CEP
 fornecido pelo usuário, utilizando a API ViaCEP.
O programa deve exibir o logradouro, bairro, cidade e estado correspondentes ao CEP consultado'''

import requests

cep = int(input("Digite o CEP (somente números): "))

#Monta a URL da API com o CEP digitado
url = f"https://viacep.com.br/ws/{cep}/json/"

response = requests.get(url)

if response.status_code == 200:
    dados = response.json()

    #Aqui faz a verificação se o CEP existe
    if 'erro' not in dados:
        logradouro = dados.get('logradouro', 'Não encontrado')
        bairro = dados.get('bairro', 'Não encontrado')
        cidade = dados.get('localidade', 'Não encontrado')
        estado = dados.get('uf', 'Não encontrado')

        print("\nInformações do ENdereço:")
        print(f"Logradouro: {logradouro}")
        print(f"Bairro: {bairro}")
        print(f"Cidade {cidade}")
        print(f"Estado: {estado}")
    else:
        print("CEP não encontrado. Verifique o número digitado.")

else:
    print(f"Erro ao consultar o CEP. Código: {response.status_code}")



