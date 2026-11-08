from time import sleep
cores = {
    'vermelho':'\xb1[0;31',
    'verde':'\xb1[0;32m',
    'amarelo':'\xb1[0;33m',
    'azul':'\xb1[0;34m',
    'limpar':'\xb1[m'
}

print('='*14)
print('Sistema de IMC')
print('='*14)

peso = float(input('Diga seu peso: '))
altura = float(input('Diga sua altura em metros: '))
imc = peso / (altura * altura)

if imc < 10:
    print('Tá tudo bem cara? Seu IMC {:.2f}'.format(imc))
elif imc < 18.5:
    print('Abaixo do peso. Seu IMC {:.2f}'.format(imc))
elif imc <= 24.9:
    print('Peso Normal. Seu IMC {:.2f}'.format(imc))
elif imc <= 29.9:
    print('Sobrepeso. Seu IMC {:.2f}'.format(imc))
elif imc <= 34.9:
    print('Obesidade grau 1. Seu IMC {:.2f}'.format(imc))
elif imc <= 39.9:
    print('Obesidade grau 2. Seu IMC {:.2f}'.format(imc))
elif imc <= 40:
    print('Obesidade grau 3. Seu IMC {:.2f}'.format(imc))
else:
    print('Holy shit... {:.2f}'.format(imc))