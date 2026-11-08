from time import sleep
cores = {
    'vermelho':'\x1b[0;31m',
    'verde':'\x1b[0;32m',
    'limpar':'\x1b[m'
} #Lista de cores

print('='*20)
print('Aprovando empréstimo')
print('='*20)

casa = float(input('Qual é o valor da casa: R$')) #Pergunta o valor da casa
salario = float(input('Qual é o seu salário: R$')) #Pergunta o salário da pessoa
anos = int(input('Em quantos anos deseja pagar: ')) #Pergunta em quantos anos deseja pagar
prestacao = casa / (anos * 12) #Faz cálculo para prestação -> Tive dificuldade de raciocinar nisso, não sei por que...
minimo = salario * 30 / 100 #Faz 30% do salario

print('Para pagar uma casa de {}R${:.2f}{} em {} anos'.format(cores['verde'], casa, cores['limpar'], anos), end=' ')
print('a prestação será de {}R${:.2f}{}'.format(cores['verde'], prestacao, cores['limpar']))
print(minimo)

if prestacao <= minimo: #Se a prestação for menor que o minimo será aceito, caso contrário não
    print('{}Empréstimo pode ser concedido.{}'.format(cores['verde'], cores['limpar']))
else:
    print('{}Empréstimo negado.{}'.format(cores['vermelho'], cores['limpar']))