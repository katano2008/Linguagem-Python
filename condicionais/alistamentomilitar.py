from datetime import date #Importação para data, dia, mês ou ano
atual = date.today().year #Configurado para dizer o ano atual
nasci = int(input('Ano de nascimento: ')) 
idade = atual - nasci 

print('Quem nasceu em {} tem {} anos em {}'.format(nasci, idade, atual))
if idade == 18:
    print('Você deve fazer o alistamento IMEDIATAMENTO!')
elif idade < 18:
    saldo = 18 - idade
    print('Você ainda não tem 18 anos, ainda faltam {} anos para o alistamento'.format(saldo))
    ano = atual + saldo
    print('Seu alistamento será {}'.format(ano))
elif idade > 18:
    saldo =idade - 18
    print('Você já deveria ter se alistado há {} anos.'.format(saldo))
    ano = atual - saldo
    print('Seu alistamento foi em {}'.format(ano))