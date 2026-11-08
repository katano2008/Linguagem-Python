from time import sleep

n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))
opcao = 0
while opcao != 5: # Enquanto variavel opcao for diferente de 5
    print('''    [ 1 ] SOMAR 
    [ 2 ] MULTIPLICAR
    [ 3 ] MAIOR
    [ 4 ] NOVOS NÚMEROS
    [ 5 ] SAIR DO PROGRAMA''')
    opcao = int(input('Qual é a sua opção? '))

    if opcao == 1:
        resultado = n1 + n2
        print('A soma de {} + {} = {}'.format(n1, n2, resultado))
        print('carregando...')
        sleep(1)
        if resultado == 67 or n1 == 67 or n2 == 67:
            print('SIXXXX SEVENNNN EBAA')
        sleep(2)
    elif opcao == 2:
        resultado = n1 * n2
        print('A multiplicação de {} x {} = {}'.format(n1, n2, resultado))
        print('carregando...')
        sleep(1)
        if resultado == 67 or n1 == 67 or n2 == 67:
            print('MEOOO DEOSS 67 SIXX SEVEENNNN!!!')
        sleep(2)
    elif opcao == 3:
        if n1 > n2:
            print('Entre {} e {} o maior valor é {}!'.format(n1,n2,n1)) 
            print('carregando...')  
            sleep(2)
        elif n2 > n1:
            print('Entre {} e {} o maior valor é {}!'.format(n1,n2,n2))
            print('carregando...')
            sleep(2)
        elif n1 == n2 or n2 == n1:
            print('Os números são iguais!')
            print('carregando...')
            sleep(2)
    elif opcao == 4:
        print('Informe os números novamente:')
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
        print('carregando...')
        sleep(2)
    elif opcao == 5:
        print('Finalizando...')
        sleep(2)
    else:
        print('Opção inválida!')
    print('=-=' * 10)
print('Fim do programa! Volte sempre!')
