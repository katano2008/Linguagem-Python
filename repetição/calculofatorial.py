import math

n = int(input('Digite um número para calcular seu fatorial: '))
c = n #contador recebe n
# f = 1
print('Calculando {}! '.format(n)) 
while c > 0: #enquanto contador for maior que 0
    print('{}'.format(c), end='') #printar o contador Ex: 6 5 4 3 2 1
    print(' x ' if c > 1 else ' = ', end='') #Se c for maior que 1 printa x, caso contrario printa =
    # f *= c #calculo fatorial
    c -= 1
print('{}'.format(math.factorial(n))) #calculo fatorial, resultado da fatorial