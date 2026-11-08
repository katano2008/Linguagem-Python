from datetime import date
atual = date.today().year #Diz em qual ano estamos
totmaior = 0 #contador maior idade
totmenor = 0 #contador menor idade
for grupo in range(1,8):
    anonasci = int(input('Em qual ano a {}ª pessoa nasceu? '.format(grupo)))
    idade = atual - anonasci
    if idade >= 21:
        totmaior += 1
    else:
        totmenor += 1
        print('Inválido')
print('Ao todo tivemos {} pessoas maiores de idade'.format(totmaior))
print('E também tivemos {} pessoas menores de idade'.format(totmenor))