num = int(input('Digite um número para ver sua tabuada: '))

for tabuada in range(1, 11):
    print('{} x {} = {}'.format(num, tabuada, num*tabuada))