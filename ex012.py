p = float(input('Qual é o preço do produto? R$'))
d = (p/100)*5
n = p-d
print('O produto passará a custar R${:.2f} com o desconto de 5%'.format(n))
