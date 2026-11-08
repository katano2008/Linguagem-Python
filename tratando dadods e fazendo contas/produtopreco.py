preco = float(input('Qual é o preço do produto? ')) #Pergunta e armazena o preço do produto com float
novo = preco - (preco * 5 / 100) #Faz o calculo do novo preço
print('O produto que custava R${}, na promoção de 5% vai custar R${}'.format(preco, novo)) #Mostra o antigo preço e agora mostra o resultado da promoção