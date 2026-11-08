from random import choice #Na caixa de ferramenta importamos a ferramenta choice
n1 = str(input('Primeiro Aluno: ')) #Pergunta e armazena o primeiro aluno em string
n2 = str(input('Segundo Aluno: ')) #Pergunta e armazena o segundo aluno em string
n3 = str(input('Terceiro Aluno: ')) #Pergunta e armazena o terceiro aluno em string
n4 = str(input('Quarto Aluno: ')) #Pergunta e armazena o quarto número em string
lista = [n1, n2, n3, n4] #Faz uma lista com os 4 alunos
escolhido = choice(lista) #Faz com o que o computador escolhe um dos 4 alunos
print('O escolhido foi {}.'.format(escolhido)) #Mostra o aluno que foi escolhido