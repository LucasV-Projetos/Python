largura = float(input('Largura da parede: '))
altura = float(input('Altura da parede: '))
area = largura * altura
print('Sua parede tem domensão de {:.2f}x{:.2f} e sua área é de {:.3f}m²'.format(largura, altura, area))
tinta = area / 2
print('Para pintar essa parede você precisará de {:.2f}l de tinta'.format(tinta))



