from time import sleep
cores = {
    'amarelo':'\x1b[0;33m',
    'verde':'\x1b[0;32m',
    'vermelho':'\x1b[0;31m',
    'fundoamarelo':'\x1b[1;33;43m',
    'limpar':"\x1b[m"
}

print('='*13)
print('{}Caixa de Loja{}'.format(cores['fundoamarelo'], cores['limpar']))
print('='*13)

valor = float(input('Qual é o valor do produto? '))
sleep(2)
forma = str(input('Qual é a forma de pagamento: Dinheiro, Pix ou Cartão? ')).lower().strip()
sleep(1)
print('Carregando...')
sleep(3)

if forma == 'dinheiro':
    novo = valor - (valor * 10/100)
    print('O valor ficou {}R${:.2f}{}'.format(cores['verde'], novo, cores['limpar']))
elif forma == 'pix':
    novo = valor - (valor * 15/100)
    print('O valor ficou {}R${:.2f}{} com uma promoção de 15%.'.format(cores['verde'], novo, cores['limpar']))
elif forma == 'cartão':
    pagamento = str(input('À vista, 2x parcelados ou até 12x parcelados? ')).lower().strip()

    if pagamento == "à vista":
        novo = valor - (valor * 5/100)
        print('O valor ficou {}R${:.2f}{} com uma promoção de 5%'.format(cores['verde'], novo, cores['limpar']))
    elif pagamento == "2x parcelados":
        novo = valor
        print('O valor ficou {}R${:.2f}{}'.format(cores['verde'], novo, cores['limpar']))
    elif pagamento == 'até 12x parcelados':
        parcela = int(input('Quantas vezes deseja parcelar? '))
        sleep(1)
        print('Carregando...')
        sleep(3)

        if 3 <= parcela <= 12:
            novo = (valor + (valor * 10/100))
            parc = novo / parcela
            print('O valor original é {}R${:.2f}{} com um aumento de 10% ficou {}R${:.2f}{}'.format(cores['verde'], valor, cores['limpar'], cores['verde'], novo, cores['limpar']))
            print('Parcelando em {}x ficou {}R${:.2f}{}'.format(parcela, cores['verde'], parc, cores['limpar']))
        else:
            print('Não dá para usar essa parcela.')
else:
    print('Forma de pagamento inválida')