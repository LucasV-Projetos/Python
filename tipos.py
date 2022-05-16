n = input('Digite algo:')

print('O tipo desse valor é:', type(n))
print('So tem espaços?', str.isspace(n))
print('É um número?', n.isnumeric())
print('É um alfabetico?', n.isalpha())
print('É um alfanumerico?', n.isalnum())
print('Está em minúsculas?', n.islower())
print('Está em maiúsculas?', n.isupper())
print('Está captalizado?', n.istitle())

