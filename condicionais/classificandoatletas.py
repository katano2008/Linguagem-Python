from datetime import date
print('=' * 21)
print('Classificando Atletas')
print('=' * 21)

nasc = int(input('Em qual ano você nasceu? '))
ano = date.today().year
idade = ano - nasc

print('O Atleta tem {} anos'.format(idade), end='|')
if idade < 0 or idade > 90:
    print('Inválido')
elif idade <= 9:
    print('Categoria: Atleta Mirim')
elif idade <= 14:
    print('Categoria: Atleta Infantil')
elif idade <= 19:
    print('Categoria: Atleta Júnior')
elif idade <= 25:
    print('Categoria: Atleta Sênior')
else:
    print('Categoria: Atleta MASTER')