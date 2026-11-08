while True:
    porta = input('A porta está fechada? [S/N] ').strip().lower()
    if porta == 's':
        certeza = input('Tem certeza? [S/N]').lower().strip()
        if certeza == 's':
            print('Porta realmente está fechada.')
        elif certeza == 'n':
            porta = input('A porta está fechada? [S/N] ').strip().lower()
    elif porta == 'n':
        certeza = input('Tem certeza? [S/N]').lower().strip()

        if certeza == 's':
            print('Porta está aberta!')
        elif certeza == 'n':
            porta = input('A porta está fechada? [S/N] ').strip().lower()
    else:
        print('resposta inválida.')