from time import sleep
termo = int(input('Me diga o primeiro termo: '))
r = int(input('Me diga a razão: '))
decimo = termo + (10 - 1) * r
print('Carregando...')
sleep(2)
for pa in range(termo, decimo + r,r):
    print('{} '.format(pa), end='-> ')
print('Acabou')