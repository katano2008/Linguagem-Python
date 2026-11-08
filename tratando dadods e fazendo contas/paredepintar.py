altura = float(input('Quanto de altura tem a parede: ')) #Pergunta e armazena a altura com float
largura = float(input('Quanto de largura tem a parede: ')) #Pergunta e armazena a largura com float
area = altura * largura #Faz o cáculo da área multiplicando largura x altura
print('A parede tem a dimensão de {}x{} e sua área é de {:.3f}m²'.format(altura, largura, area)) #Mostra a altura e largura e logo o resultado da area
tinta = area / 2 #Calculo da quantidade de tinta necessária para pintar a parede
print('Para pintar essa parede, você precisará de {}l de tinta.'.format(tinta)) #Mostra o resultado da tinta necessária