contador = 0
for numeros in range(1, 11):
    num = int(input('Digite o {}ª: '.format(numeros)))
    if num > 10:
        contador += 1
print('Foram encontrados {} números maiores que 10.'.format(contador))