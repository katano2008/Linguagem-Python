from random import randint
from time import sleep

cores = {
    'verde':'\x1b[1;32m',
    'vermelho':'\x1b[1;31m',
    'amarelo':'\x1b[1;33m',
    'fundobranco':'\x1b[1;30;47m',
    'limpar':'\x1b[m'
}

print('{}{:=^22}{}'.format(cores['amarelo'], 'Jokenpô', cores['limpar']))
print('{}Pedra, Papel e Tesoura{}'.format(cores['fundobranco'], cores['limpar']))
print('{}={}'.format(cores['amarelo'], cores['limpar']) *22)

player = int(input('''Escolha uma das opções: 
[ 0 ] Pedra
[ 1 ] Papel
[ 2 ] Tesoura
Qual será sua escolha? '''))
print('Computador está escolhendo agora... Aguarde!')
sleep(3)
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ!')
sleep(1)

escolha = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0,2)
print('-=-' *11)
print('O computador escolheu {}.'.format(escolha[computador]))
print('O jogador escolheu {}.'.format(escolha[player]))
print('-=-' *11)

if computador == 0: #Computador escolheu Pedra
    if player == 0:
        print('{}EMPATADO!{}'.format(cores['amarelo'], cores['limpar']))
    elif player == 1:
        print('{}JOGADOR GANHOU!{}'.format(cores['verde'], cores['limpar']))
    elif player == 2:
        print('{}jogador perdeu...{}'.format(cores['vermelho'], cores['limpar'])) 
    else:
            print('Escolha Inválida')
elif computador == 1: #Computador escolheu Papel
    if player == 0:
        print('{}jogador perdeu...{}'.format(cores['vermelho'], cores['limpar']))
    elif player == 1:
        print('{}EMPATADO!{}'.format(cores['amarelo'], cores['limpar']))
    elif player == 2:
        print('{}JOGADOR GANHOU!{}'.format(cores['verde'], cores['limpar']))
    else:
            print('Escolha Inválida')
elif computador == 2: #Computador escolheu Tesoura
    if player == 0:
        print('{}JOGADOR GANHOU!{}'.format(cores['verde'], cores['limpar']))
    elif player == 1:
        print('{}jogador perdeu...{}'.format(cores['vermelho'], cores['limpar']))
    elif player == 2:
        print('{}EMPATADO!{}'.format(cores['amarelo'], cores['limpar']))
    else:
        print('Escolha Inválida')