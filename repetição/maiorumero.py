maiornum = 0

for maioridade in range(1, 6):
    num = int(input('{}ª)  Escolha um número: '.format(maioridade)))
    if maioridade == 1:
        maiornum = num
    else:
        if num > maiornum:
            maiornum = num
print('O maior número foi {}.'.format(maiornum))