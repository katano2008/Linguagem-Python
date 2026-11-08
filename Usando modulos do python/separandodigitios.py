# Separando digitos com import random, achei que seria legal também. Mas, logo abaixo deixei com opção da pessoa também conseguir responder
from random import randint #Na caixa de ferramenta random importamos a ferramenta randint

# num = int(input('Digite um número de 0 a 9999: ')) Diz e armazena um número de 0 a 9999 em número Inteiro
# n = str(num) #Transforma a variavel num em uma string

num = randint(0, 9999) #faz uma variavel num e faz com o que o computador escolha um número de 0 a 9999 com randint
n = str(num) #Transforma a variavel num em string
print('Analisando o número {}'.format(num)) #Mostra que está analisando a variavel
print('Unidade: {}'.format(n[3])) #Mostra a unidade
print('Dezena: {}'.format(n[2])) #Mostra a dezena
print('Centena: {}'.format(n[1])) #Mostra a centena
print('Milhar: {}'.format(n[0])) #Mostra o milhar