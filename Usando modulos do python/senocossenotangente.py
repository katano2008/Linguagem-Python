# import math #Importação da caixa de ferramente math
from math import sin, cos, tan, radians
ang = float(input('Digite um angulo que você deseja: ')) #Pergunta e armazena o ângulo desejado em float
sen = sin(radians(ang)) #Com a ferramenta sin e radians é calculado o seno do angulo
coss = cos(radians(ang)) #Com a ferramenta cos e radians é calculado o cosseno do angulo
tg = tan(radians(ang)) #Com a ferramenta tan e radians é calculado a tangente do angulo
print('O ângulo de {} tem o Seno {:.2f}.'.format(ang, sen)) #Mostra o angulo e o seno dele
print('O ângulo de {} tem o Cosseno {:.2f}.'.format(ang, coss)) #Mostra o angulo e o cosseno dele
print('O ângulo de {} tem a Tangente {:.2f}.'.format(ang, tg)) #Mostra o angulo e a tangente dele