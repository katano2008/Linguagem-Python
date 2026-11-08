frase = 'Curso em Vídeo Python'
frase.count('o') #vai contar quantos "o" tem na variante frase
frase.find('deo') #vai procurar "deo" na variante frase
frase.len(frase) #vai mostrar quantos caracteres tem a frase
frase.find('android') #vai procurar a palavra "android" na variavel frase, resultando em -1, por que não tem.
'curso' in frase # Vai analisar se tem curso na variavel frase
frase.replace('Python', 'Android') #vai trocar python por android na variante frase
frase.upper(frase) #Transformar a frase em maiusculo
frase.lower(frase) #Transformar a frase em minusculo
frase.capitalize(frase) #Deixar apenas a primeira letra em maisculo
frase.title(frase) #vai analisar quantas palavras tem a string
frase.strip(frase) #vai remover todos os espaços inuteis da variante frase, como espaçamento no inicio e fim.
frase.rstrip(frase) #O lado direito da string, vai ter o espaçamento removido (o espaçamento final removido)
frase.lstrip(frase) #O lado esquerdo da string, vai ter o espaçamento removido (o espaçamento inicial removido)
'-'.join(frase) #Juntar uma palavra com a outra

print('''aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa''') #As três aspas serve para textos grandes de outras linhas