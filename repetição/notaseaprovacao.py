from time import sleep

cores = {'Vermelho':'\033[31m',
        'Verde':'\033[32m',
        'Amarelo':'\033[33m',
        'limpar':'\033[m' 
}

somaMed = 0
maiornota = 0
aprovado = 0
reprovado = 0
for alunos in range(1,7):
    nota = float(input('Nota do {}ª aluno: '.format(alunos)))
    sleep(1)
    print('carregando...')
    sleep(3)
    
    if nota < 0 or nota > 10: #Verifica se a nota está fora  do intervalo permitido
        print('{}Nota Inválida!{} {}ERRO NO CÓDIGO{}'.format(cores['Amarelo'], cores['limpar'], cores['Vermelho'], cores['limpar']))
        break #Encerra o for porque a nota não é válida

    if alunos == 1: # Primeiro looping ( CODIGO DE MAIOR NOTA )
        maiornota = nota #Armazenar a nota do primeiro looping como maior nota
    elif nota > maiornota: #Se não a nota de outro aluno for maior
            maiornota = nota #Irá se tornar a maior nota

    if nota >= 6: # Se nota for maior ou igual a 6
        aprovado += 1 # +1 aprovado
    if nota < 6: # Se nota for menor que 6
        reprovado += 1 # +1 reprovado

    if nota < 6:
        print('{}REPROVADO{}'.format(cores['Vermelho'], cores['limpar']))
    else:
        print('{}APROVADO{}'.format(cores['Verde'], cores['limpar']))

    somaMed += nota

media = somaMed / 6
print('A média da turma foi: {:.2f}'.format(media))
print('Alunos aprovados: {}'.format(aprovado))
print('Alunos reprovados: {}'.format(reprovado))
print('Maior nota: {}'.format(maiornota))