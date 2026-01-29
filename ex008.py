m = float(input('Distância em metros: '))
km = m/1000
hm = m/100
dam = m/10
dm = m * 10
cm = m * 100
mm = m * 1000
print('A conversão de {} metros é: '.format(m))
print('Kilometros: {}km \nHectômetros: {}hm \nDecâmetros: {}dam \nDecímetros: {}dm \nCentímetros: {}cm \nMilímetros: {}mm'.format(km,hm,dam,dm,cm,mm))
