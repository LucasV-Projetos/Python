i = int(input('Informe um número entre 0 a 999: '))
str(i)
u = i // 1 % 10
d = i // 10 % 10
c = i // 100 % 10
m = i // 1000 % 10
print('Unidade: {}'.format(u))
print('Unidade: {}'.format(d))
print('Unidade: {}'.format(c))
print('Unidade: {}'.format(m))