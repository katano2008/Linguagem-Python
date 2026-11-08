ca = int(input('Quantos dias o carro foi alugado? ')) #Pergunta quantos dias foi alugado.
km = float(input('Quantos Km o carro rodou? ')) #Pergunta quanto o carro rodou.
pago = (ca * 60) + (km * 0.15) #Faz o cálculo do orçamento final, com as taxas de 60 reais (tempo alugado) e 0,15 reais (Quantidade que o carro rodou)
print('O preço será {:.2f}'.format(pago)) #Mostra o resultado final com uma resposta