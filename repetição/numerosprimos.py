cor = {
    'vermelho':'\033[31m',
    'amarelo':'\033[33m',
    'limpar':'\033[m'
}
primo  = int(input('Digite um número: '))
total = 0 #Contador de número divisíveis
for i in range(1, primo + 1):
    if primo % i == 0: #Se variavel primo e o i ter o resto 0, mostrará os números primos
        print(cor['vermelho'], end='') #Mostrará os números primos com cores
        total += 1 #Contador de números divisíveis, adicionando.
    else: #Caso contrário
        print(cor['amarelo'], end='') #Mostrará os números que não são primos de outra cor
    print('{} '.format(i), end='')
print('{}O número {} foi divisível {} vezes'.format(cor['limpar'], primo, total))

#Sabendo que % é o resto da divisão podemos pensar em 8 / 4 = 2, mas 8 % 4 = 0 e 8 // 4 = 2