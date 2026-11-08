from time import sleep

cor = {
    'verde':'\x1b[0;32m',
    'vermelho':'\x1b[0;31m',
    'amarelo':'\x1b[0;33m',
    'fundobranco':'\x1b[1;30;40m',
    'limpar':'\x1b[m'
}

print('=' * 26)
print('{}Gerenciamento de Pagamento{}'.format(cor['amarelo'], cor['limpar']))
print('{:=^26}'.format('Lojas Katano'))
print('=' * 26)

produto = float(input('Preço das compras: R$'))
sleep(1)
forma = int(input('''FORMAS DE PAGAMENTOS
[{} 1 {}] À vista dinheiro ou Cheque
[{} 2 {}] À vista no cartão
[{} 3 {}] Em até 2x no cartão
[{} 4 {}] 3x ou mais no cartão
Escolha uma dessas opções: '''.format(cor['fundobranco'], cor['limpar'], cor['fundobranco'], cor['limpar'], cor['fundobranco'], cor['limpar'], cor['fundobranco'], cor['limpar'])))
print('Carregando...')
sleep(2)

if forma == 1:
    total = produto - (produto * 10/100)
    print('O pagamento foi Dinheiro/Cheque, com o Desconto de 10% sua compra ficou {}R${:.2f}{}.'.format(cor['verde'], total, cor['limpar']))
elif forma == 2:
    total = produto - (produto * 5/100)
    print('O pagamento foi À vista no cartão, com desconto de 5% sua compra ficou {}R${:.2F}{}.'.format(cor['verde'], total, cor['limpar']))
elif forma == 3:
    total = produto
    parcela = total / 2
    print('O pagamento foi em até 2x no cartão, sem JUROS. A compra ficou {}R${:.2f}{}.'.format(cor['verde'], parcela, cor['limpar']))
elif forma == 4:
    total = produto + (produto * 20/100)
    totalparc = int(input('Deseja parcelar em até quantas vezes? '))
    parcela = total / totalparc
    sleep(2)
    if parcela >= 3:
        print('O pagamento foi parcelado em {}x, com 20% de JUROS. A compra ficou {}R${:.2f}{}.'.format(totalparc ,cor['verde'], parcela, cor['limpar']))
    else:
        print('{}Inválido.{}'.format(cor['vermelho'], cor['limpar']))
else:
    total = produto
    print('{}Opção Inválida!{}'.format(cor['vermelho'], cor['limpar']))
print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(produto, total))