n1 = int(input('Um valor: ')) #Pergunta e armazena o número inteiro e pede um valor
n2 = int(input('outro valor:')) #Pergunta e armazena o número inteiro e pede o segundo valor
s = n1 + n2 #Faz a somatória do n1 e n2
m = n1 * n2 #Faz a multiplicação do n1 e n2
d = n1 / n2 #Faz a divisão do n1 e n2
di = n1 // n2 #Faz a divisão inteira do n1 e n2
e = n1 ** n2 #Faz a potencia de n1 e n2
print('A soma é  {},\n o produto é {} e\n a divisão é {:.3f}'.format(s, m, d), end='  ') #Mostra o resultado da soma, multiplicação e da divisão e no final (end) faz com que continue na mesma linha invés de pular outra linha
print('Divisão inteira {} e potência {}'.format(di, e)) #Mostra o resultado da divisão inteira e da potência