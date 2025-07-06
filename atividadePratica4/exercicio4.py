'''
Exercicio 4: Crie um programa que consulte a cotação atual de uma moeda estrangeira em relação
ao Real Brasileiro (BRL). O usuário deve informar o código da moeda desejada (ex: USD, EUR, GBP),
e o programa deve exibir o valor atual, máximo e mínimo da cotação, além da data e hora da última atualização.
Utilize a API da AwesomeAPI para obter os dados de cotação.​'''

import requests

moeda = input("Digite o código da moeda (ex: USD, EUR, GBP): ").upper()

#Monta a URL da API
url = f"https://economia.awesomeapi.com.br/json/last/{moeda}-BRL"

try:
    response = requests.get(url, timeout=5)
    response.raise_for_status()

    dados = response.json()
    chave = f"{moeda}BRL"

    if chave in dados:
        cotacao = dados[chave]

        valor_atual = cotacao.get('bid', 'N/A')
        valor_maximo = cotacao.get('high', 'N/A')
        valor_minimo = cotacao.get('low', 'N/A')
        data_hora = cotacao.get('create_date', 'N/A')

        print(f"\nCotação de {moeda} para BRL:")
        print(f"Valor Atual: R$ {valor_atual}")
        print(f"Valor Máximo do Dia: R$ {valor_maximo}")
        print(f"Valor Mínimo do Dia: R$ {valor_minimo}")
        print(f"Data e HOra da Última Atualização: {data_hora}")
    else:
        print("Moeda não encontrada. Verifique o código informado.")

except requests.exceptions.Timeout:
    print("Erro: Tempo de conexão esgotado. Tente novamente.")
except requests.exception.RequestException as e:
    print(f"Erro ao acessar a API: {e}")
