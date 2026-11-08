print('=' * 20)
print('Aumentos múltiplos')
print('=' * 20)

nome = str(input('Qual seu nome? '))
salario = float(input('Qual seu salário? '))

if salario <= 1250:
    novo = salario + (salario * 15/100)
else:
    novo = salario + (salario * 10/100)
print('Olá {}! Seu salário era R${:.2F} e agora teve um aumento de R${:.2f}'.format(nome, salario, novo))