soma = 0
cont = 0
for somatoria in range(1,7):
    num = int(input('Digite o {} valor: '.format(somatoria)))
    if num % 2 == 0:
        soma += num
        cont += 1
    if num == 67:
        print('SIXXXXXXXX SEVEEEEEEEENNNNNN!!!!')
print('Você disse {} números pares e a soma foi {}'.format(cont, soma))
