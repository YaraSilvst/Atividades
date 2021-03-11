import math 

def coeficientes(a, b, c):

	delta = (b * b) - 4 * a * c

	print('Valor de Delta:' ,delta)

	if delta < 0:
		print('A equação não possui raízes reais')

	elif delta <= 0:
		print(delta) 

	else:

		x = (-b + math.sqrt(delta) / 2) * a
		print(x)

		x2 = (-b - math.sqrt(delta) / 2) * a
		print(x2)






