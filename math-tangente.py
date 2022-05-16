import math

an = float(input('Digite o ángulo que deseja: '))
se = math.sin(math.radians(an))
co = math.cos(math.radians(an))
ta = math.tan(math.radians(an))
print('O ângulo de {} tem o SENO de {:.2f}'.format(an, se))
print('O ângulo de {} tem o COSSENO DE {:.2f}'.format(an, co))
print('O ângulo de {} tem o a TANGENTE de {:.2f}'.format(an, ta))
