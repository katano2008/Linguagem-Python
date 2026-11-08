from random import shuffle #Na caixa de ferramenta random importamos shuffle
n1 = str(input('Primeiro Aluno: ')) #Pergunta e armazena o primeiro aluno em string
n2 = str(input('Segundo Aluno: ')) #Pergunta e armazena o segundo aluno em string
n3 = str(input('Terceiro Aluno: ')) #Pergunta e armazena o terceiro aluno em string
n4 = str(input('Quarto Aluno: ')) #Pergunta e armazena o quarto aluno em string
lista = [n1, n2, n3, n4] #Faz uma lista com os 4 alunos
shuffle(lista) #Bagunça/embaralha a ordem da lista com shuffle, ou seja, shuffle = embaralha
print('A sequência é {}'.format(lista)) #Mostra a sequência de alunos no qual foi embaralhado com shuffle