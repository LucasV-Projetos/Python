i = float(input('Uma distância em metros: '))
print('A medida de {:.1f}m corresponde a'.format(i))

km = i/1000
print('{}km'.format(km))

hm = i/100
print('{}hm'.format(hm))

dam = i/10
print('{}dam'.format(dam))

dm = i*10
print('{:.0f}dm'.format(dm))

cm = i*100
print('{:.0f}cm'.format(cm))

mm = i*1000
print('{:.0f}mm'.format(mm))
