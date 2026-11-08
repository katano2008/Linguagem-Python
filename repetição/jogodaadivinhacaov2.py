from random import randint
from time import sleep
computer = randint(0,10) # Computador escolhe número de 0 a 10
print('Sou seu computador, Acabei de pensar em um número de 0 a 10. Será que você consegue adivinhar?')
tentativa = 0 #Contador de tentativas
acertou = False #Acertou recebe falso

while not acertou: #Enquanto não acertou
    player = int(input('Escolha um número de 0 a 10: ')) 
    tentativa += 1 # Tentativa recebe mais 1
    if player == computer: #Se player for igual a computador
        acertou = True #Acertou recebe verdadeiro e acaba o jogo
    else: #Caso contrário
        if player < computer: #Se player for menor que computador
            print('Mais... Manda outra pivete') #printa que o número escolhido é maior
        elif player > computer: #Se não player for maior que computador
            print('Menos... Manda mais uma ae carae') #Printa que o número escolhido é menor
print('Acertou com {} tentativas! Parabéns'.format(tentativa)) 