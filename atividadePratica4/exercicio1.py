'''Exercicio 1: Crie um programa que gera uma senha aleatória com o módulo random,
    utilizando caracteres especiais, possibilitando o usuário a informar a quantidade
    de caracteres dessa senha aleatória. ​'''

import random
import string

tamanho = int(input("Digite o tamanho desejado para a senha: "))

#Define os caracteres possíveis: letras, números e símbolos
caracteres = string.ascii_letters + string.digits + string.punctuation

#aqui gera a senha aleatória
senha = ''.join(random.choice(caracteres) for _ in range(tamanho))

print(f"Senha gerada: {senha}")
