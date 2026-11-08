gen = str(input('Informe seu Sexo: [M/F] ')).strip().upper()[0]
while gen not in 'MmFf': #Enquanto gen não estiver em Masculino [M] ou feminino [F]
    gen = str(input('Dados inválidos. Por favor, informe seu sexo: [M/F] ')).strip().upper()[0]
print('Gênero {} registrado com sucesso'.format(gen))
