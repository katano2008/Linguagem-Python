print('=' * 20)
print('Classificação de Idade')
print('=' * 20)

idade = int(input('Quantos anos você tem? '))

if idade < 0:
    print('Uai um feto? Que pressa para nascer!')
elif idade <= 12:
    print('Você é uma criança!')
elif idade < 18:
    print('Você é um aborrecente...')
elif idade <= 59:
    print('Você já é uma adulto.')
elif idade < 100:
    print('O senhor já idoso, longa vida teve.')
else:
    print('Que porra é essa? Virou imortal?!')