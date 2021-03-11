def eleicao():


	candidatos = ["1- Candidato A", "2- Candidato B", "3- Candidato C", "4- Nulo", "5- Branco"]
	resultado_voto = [0,0,0,0,0]
	votos = []

	for cont in range (3):

		for opcao in candidatos:
			print(opcao)

		voto =  int (input('Em quem deseja votar?\n'))
		votos.append(voto)
		print(votos)


	for v in votos:
		if v == 1:
			resultado_voto[0] +=1
		elif v == 2:
			resultado_voto[1] +=1
		elif v == 3:
			resultado_voto[2] +=1
		elif v == 4:
			resultado_voto[3] +=1
		else:
			resultado_voto[4] +=1


	print('Candidato A obteve: %s' % (resultado_voto[0]))
	print('Candidato B obteve: %s' % (resultado_voto[1]))
	print('Candidato C obteve: %s' % (resultado_voto[2]))
	print('Votos Nulos: %s' % (resultado_voto[3]))
	print('Votos em branco: %s' % (resultado_voto[4]))

	if resultado_voto[3] >= 0:
		print((resultado_voto[3] * 100) / 3)

	else:
		print('0 votos nulos')

	if resultado_voto[4] >= 0:
		print((resultado_voto[4] * 100) / 3)

	else:
		print('0 votos brancos')



		



	










