import math
a = float(input('Digite o ângulo que você deseja: '))
sen = math.sin(math.radians(a))
cos = math.cos(math.radians(a))
tan = math.tan(math.radians(a))
print(f'SENO: {sen:.2f}\nCOSSENO: {cos:.2f}\nTANGENTE: {tan:.2f}')
