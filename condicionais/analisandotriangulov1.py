print('=' * 20)
print('Analisando triangulo V1.0')
print('=' * 20)

r1 = float(input('Primeiro Segmento: '))
r2 = float(input('Segundo Segmento: '))
r3 = float(input('Terceiro Segmento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Forma um triângulo!')
else:
    print('Não forma um triângulo...')