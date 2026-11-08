import random

print('=' * 20)
print('Positivo ou Negativo')
print('=' * 20)

n = int(input('Escolha um número: '))

if n > 0:
    print('O número é Positivo!')
elif n == 0:
    print('O número é Zero.')
else:
    print('O número é negativo.')