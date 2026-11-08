from math import hypot #De Math importamos hypot, pegamos uma ferramenta especifica dentro de uma caixa de ferramentas
ca = float(input('Qual o comprimento do cateto adjacente? ')) #Pergunta o comprimento do cateto adjacente
co = float(input('Qual o comprimento do cateto oposto? ')) #Pergunta o comprimento do cateto oposto
tg = hypot(co, ca) #Com a ferramenta importada calculamos a hipotenusa/tangente
print('A hipotenusa do triangulo é {:.2f}'.format(tg)) #Mostra o resultado final com uma resposta