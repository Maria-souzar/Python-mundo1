import math
co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
hipotenusa = math.hypot(co,ca)
print(f'A hipotenusa vai medir {hipotenusa:.2f}')
