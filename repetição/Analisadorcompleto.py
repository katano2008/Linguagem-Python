from time import sleep
# VARIAVEIS
adidade = 0 #Somatória de idade, contabilizador 0
mediaidade = 0 #media da idade, variavel no qual armazena
maioridadeH = 0 #maior valor encontrada entre os homens
nomevelho = '' #nome da pessoa mais velha
totmulher20 = 0 #Contador de quantas mulheres menor de 20 anos

#REPETIÇÃO
for cadastro in range(1,5):
    print('----- {}ª PESSOA -----'.format(cadastro))
    name = str(input('Nome: ')).strip()
    age = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).lower().strip()
    adidade += age
    if cadastro == 1 and sexo in 'm': #Se o primeiro cadastro tiver m em sexo
        maioridadeH = age #Usa a idade do primeiro homem como referência
        nomevelho = name #Guarda o nome do primeiro homem como referência
    if sexo in 'm' and age > maioridadeH: #Se m estiver em sexo e idade for maior a maioridadeH
        maioridadeH = age #Atualiza a maior idade encontrada entre homens
        nomevelho = name #Atualiza o nome do homem mais velho
    if sexo in 'f' and age < 20: #Se tiver F em sexo e idade for menor que 20
        totmulher20 += 1 #Adicione mais 1 na variavel totmulher20

#CONCLUSÃO
mediaidade = adidade / 4 #media da idade do grupo, a soma das idades dividido pela quantidade de pessoas
print('A média de idade do grupo é de {} anos'.format(mediaidade))
print('O homem mais velho tem {} anos e se chama {}'.format(maioridadeH, nomevelho))
print('Ao todo são {} mulheres com menos de 20 anos'.format(totmulher20))
