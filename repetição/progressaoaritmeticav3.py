termo = int(input('Qual é o termo? '))
razao = int(input('Qual é a razão? '))
cont = 1 
mais = 10 #limite de até mais 10 termos na questão
total = 0 #armazenamento de total conforme a quant. de termos
while mais != 0: #enquanto mais for diferente de 0
    total += mais #some total e mais
    while cont <= total: #enquanto contagem for menor ou igual a total
        print('{} -> '.format(termo), end='') 
        termo += razao # somatória de termo e razão
        cont += 1 #contagem de termos
    print('PAUSA')
    mais = int(input('Quantos termos você quer mostrar a mais? ')) #pergunta se deseja mais termos e armazena mais no inicio da repetição
print('Progressão realizada com {} termos'.format(cont)) #mostra quantos termos foram ditos