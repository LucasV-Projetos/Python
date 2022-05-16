f = 123.95  # float(input('Qual é o preço do produto? R$'))
promo = f - f * 5 / 100
print(('O produto que custava R${}, na promoção com desconto de 5% vai custar RS{:.2f}'.format(f, promo)))