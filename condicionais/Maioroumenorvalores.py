print('=' * 22)
print('Maior ou Menor valores')
print('=' * 22)

n1 = int(input('Primeiro número: '))
n2 = int(input('Segundo número: '))
n3 = int(input('Terceiro número: '))

#verificando MENOR
menor = n1
if n2 < n3 and n2 < n1:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3

#Verificando MAIOR
maior = n1
if n2 > n3 and n2 > n1:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3

print('O menor número é {}'.format(menor))
print('O maior número é {}'.format(maior))