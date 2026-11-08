from math import ceil

n1 = float(input("Primeira nota: "))
n2 = float(input("Segunda nota:"))
m = (n1 + n2) / 2

if m >= 7:
    print("PARABÉNS PELO {:.2f}! Passou de ano.".format(m))
else:
    print("Que pena pelo seu {:.2f}... Talvez em uma outra oportunidade.".format(m))