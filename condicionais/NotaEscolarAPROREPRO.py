cores = {
    'vermelho':'\x1b[0;31m',
    'VermelhoBold':'\x1b[1;31m',
    'amarelo':'\x1b[0;33m',
    'verde':'\x1b[0;32m',
    'limpar':'\x1b[m'
}

print('=' * 31)
print('\033[0;37;40mNota Escolar Aprovado/Reprovado\033[m')
print('=' * 31)

nota1 = float(input('Primeira nota do aluno: '))
nota2 = float(input('Segunda nota do aluno:'))
nota3 = float(input('Terceira nota do aluno: '))
media = (nota1 + nota2 + nota3) / 3

if media < 0 or media > 10:
    print('{}Nota Inválida!{}'.format(cores['VermelhoBold'], cores['limpar']))
elif media <= 4.9:
    print('{}Reprovado {:.2f}{}!'.format(cores['vermelho'], media, cores['limpar']))
elif media <= 6.9:
    print('{}Recuperação {:.2f}.{}'.format(cores['amarelo'], media, cores['limpar']))
else:
    print('{}APROVADO! Nota {:.2f}{}'.format(cores['verde'], media, cores['limpar']))