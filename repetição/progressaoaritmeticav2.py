termo = int(input('Primeiro termo: '))
r = int(input('Razão da PA: '))
cont = 1 #contagem começa em 1
while cont <= 10: #enquanto contagem for menor ou igual a 10
    print('{} -> '.format(termo), end='') #printa o termo com uma seta para o lado
    termo += r #Termo mais razao. Ex: Se o termo é 2 e a razão é 2 então 2 4 6 8 10
    cont += 1 #variavel cont recebe mais 1 até ficar igual a 10
print('fim')