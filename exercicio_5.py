def valores (a, b, c):

	medida1 = a
	medida2 = b
	medida3 = c

	if (a + b) < c:
		print('Formam um triângulo')

	elif (a + c) < b:
		print('Formam um triângulo')

	elif (b + c) < a:
		print('Formam um triângulo')

	else:
	print('Não formam um triângulo')