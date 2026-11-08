nome = input('Qual seu nome completo? ') #Pergunta o nome completo
print('Seu nome em maiúsculas é {}'.format(nome.upper())) #Mostra o nome completo tudo maiúsculo
print('Seu nome em minúsculas é {}'.format(nome.lower())) #Mostra o nome completo tudo minúsculo
print('Seu nome tem ao todo {} letras'.format(len(nome) - nome.count(' '))) #Mostra quantas letras tem sem contar com os espaços
# print('Seu primeiro nome tem {} letras'.format(nome.find(' '))) -> Mostra quantas letras tem o primeiro nome
separa = nome.split() #Armazena a variavel sem espaços no lado esquerdo e direito
print('Seu primeiro nome é {} e ele tem {} letras'.format(separa[0], len(separa[0]))) #Mostra quantas letras tem o primeiro nome