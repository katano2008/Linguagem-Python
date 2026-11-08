nome = input('Qual o nome do funcionário? ') #Pergunta e armazena o nome do funcionario
Sa = float(input('Qual o salário atual? ')) #Pergunta e armazena o salário atual em float
novo = Sa + (Sa * 15 / 100) #Faz o calculo do novo salário, ou seja, um reajuste salarial
print('O salário de {} era R${:.2f} e com o reajuste de 15% vai passar a receber R${:.2f}'.format(nome, Sa, novo)) #Mostra o nome do funcionário, qual era o salário dele e quanto irá receber agora