print('=-'*10)
print('Sistema de segurança')
print('=-'*10)

tentativa = 3
senha_correta = '0506'
cores = {'verde':'\033[32m',
        'vermelho':'\033[31m',
        'amarelo':'\033[1;33m',
        'limpar':'\033[m'         
}
while not tentativa == 0: #Enquanto tentativa não for igual a zero
    senha = str(input('Digite a senha: ')) #Pergunte novamente a senha ou pergunte
    
    if senha == senha_correta: #Se senha for igual a senha correta
        print(f'{cores["verde"]}Acesso Liberado!{cores["limpar"]}') #Acesso será liberado
        break #Repetição while finaliza
    else: #Caso contrário 
        if senha != senha_correta: # Se Senha for diferente de senha correta
            tentativa -= 1 #Diminui uma tentativa
            print(f'{cores["amarelo"]}Acesso negado. Você tem {tentativa} tentativas.{cores["limpar"]}') #Informe que o acesso foi negado

else: #Caso contrário, caso o tentativa seja igual a 0
    print(f'{cores["vermelho"]}Acesso Bloqueado!{cores["limpar"]}') #Informe que o acesso foi bloqueado
