frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split() #Separa em palavras
junto = ''.join(palavras) #Junta a frase
inverso = junto[::-1] #Inverte a frase

'''for letra in range(len(junto) - 1, -1, -1 ):  #Repetição no qual inverte a frase
    inverso += junto[letra]'''

if inverso == junto:
    print('Temos um palíndromo')
else:
    print('Não temos um palíndromo')