print('=' * 20)
print('Par ou Impar')
print('=' * 20)

n = int(input('Escolha um número: '))
resultado = n % 2

if resultado == 0:
    print('O número {} é par'.format(n))
else:
     print('O número {} é impar'.format(n))


# if (n % 2 == 0):
#     print('O número {} é par'.format(n))
# else:
#     print('O número {} é impar'.format(n))