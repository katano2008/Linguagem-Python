from time import sleep
cor = {
    'vermelho':'\x1b[0,31m',
    'limpar':'\x1b[m'
}
for tempo in range(10, -1, -1): #Uma repetição em um intervalo de 10 até 0.
    print(tempo)
    sleep(1)
print('{}KAAAAAAAABUMMMMMMMMMMMMMMMMMMM BOOWWWWWWWWWWWWWWW!!!{}'.format(cor['vermelho'], cor['limpar']))