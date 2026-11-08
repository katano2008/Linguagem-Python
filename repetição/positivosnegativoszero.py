positivo = 0 
negativo = 0 
zero = 0 
somaPos = 0  
somaNeg = 0
for numbers in range(1, 11):
    numero = int(input('Digite o {}ª número: '.format(numbers)))
    if numero > 0: # VERIFICAR QUANT. NUMEROS POSITIVOS
        positivo += 1
        somaPos += numero
    elif numero < 0: # VERIFICAR QUANT. NUMEROS NEGATIVOS
        negativo += 1
        somaNeg += numero
    else: # VERIFICAR QUANT. DE ZEROS
        zero += 1

print('Números Positivos: {}'.format(positivo)) # Dirá quant. de numeros positivos
print('Números Negativos: {}'.format(negativo)) # Dirá quant. de numeros negativos
print('Zeros: {}'.format(zero)) # Dirá quant. de zeros
print('Soma dos positivos: {}'.format(somaPos)) # Vai apresentar a somatória dos numeros positivos
print('Soma dos negativos: {}'.format(somaNeg)) # Vai apresentar a somatória dos numeros negativos