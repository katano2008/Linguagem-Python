from random import randint
from time import sleep
computador = randint(0,5)

print('=' * 20)
print('JOGO DE ADIVINHAÇÃO')
print('=' * 20)

jogador = int(input('Vou pensar em um número de 0 até 5. Tente adivinhar! '))
print('PROCESSANDO...')
sleep(3)

if jogador == computador:
    print('PARABÉNS, VOCÊ VENCEU!')
else:
    print('EU GANHEI! pensei no {} e não {}'.format(computador, jogador))