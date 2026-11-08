# EXEMPLO 1
c = 1

while c < 10:
    print(c)
    c += 1
print(c)

# EXEMPLO 2
r = 'S'
while r == 'S':
    n = int(input('Escolha um número: '))
    r = str(input('Deseja continuar? [S/N]')).upper()
print('FIM')

# EXEMPLO 3
n = 1
par = 0
impar = 0
while n != 0: # Enquanto n for diferente de 0
    n = int(input('Digite um valor: '))
    if n != 0: # Se n for diferente de 0
        if n % 2 == 0: # Se o resto de N e 2 for 0
            par += 1 #mais um par
        else: # caso contrario
            impar += 1 #mais um impar
print('Você digitou {} números pares e {} números impares.'.format(par, impar))

# EXEMPLO 4
senha_correta = '0506'
tentativa = 3
while tentativa <= 0:
    senha =  int(input('Digite a senha: '))
    if senha == senha_correta:
        print('Acesso liberado')
    else:
        if senha != senha_correta:
            tentativa -= 1
else:
    print('Acesso Bloqueado!')