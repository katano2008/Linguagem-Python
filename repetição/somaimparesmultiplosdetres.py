soma = 0 #variavel de soma no qual a soma começa no 0
cont = 0 #variavel de contagem no qual a contagem tem seu ponto inicial em 0
for impar in range(1, 501, 2): # Repetição de 1 até 501 pulando de 2 em 2 de forma intencional para ver os números ímpares
    if impar % 3 == 0: #questiona se o resto da divisão é igual zero?
        cont = cont + 1 #Faz a contagem de 1 em 1
        soma += impar #somatória de todos os numeros de impar
print('A soma de todos os {} valores solicitados é {}'.format(cont, soma))