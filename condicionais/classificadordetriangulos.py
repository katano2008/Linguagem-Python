from time import sleep
cores = {'amarelo':'\x1b[0;33m',
            'verde':'\x1b[0;32m',
            'vermelho':'\x1b[0;31m',
            'azul':'\x1b[0;34m',
            'limpar':'\x1b[m',
            'amarelofundo':'\x1b[1;33;43m'
        }

print('=' * 27)
print('{}Classificador de Triangulos{}'.format(cores['amarelofundo'], cores['limpar']))
print('=' * 27)

l1 = int(input('Qual o valor da primeira reta? '))
sleep(2)
l2 = int(input('Qual o valor da segunda reta? '))
sleep(2)
l3= int(input('Qual o valor da terceira reta? '))
print('{}Armazenando valores...{}'.format(cores['amarelo'], cores['limpar']))
sleep(3)

if l1 < l2 + l3 and l2 < l1 + l3 and l3 < l1 + l2:
    print('{}É um triângulo{}'.format(cores['verde'], cores['limpar']))
    if l1 == l2 == l3:
        print('É Equilatéro')
    elif l1 == l2 != l3 or l1 != l2 == l3 or l1 == l3 != l2:
        print('É Isoceles')
    else:
        print('É Escaleno')
else:
    print('{}Não é um triângulo!{}'.format(cores['vermelho'], cores['limpar']))