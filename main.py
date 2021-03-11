from eleicao_classes import *

op = 10

while op != 0:
	print("-------------------------\n")
	print("    DIGITE UMA OPÇÃO     \n")
	print("-------------------------\n")
	print(" 1 - Cadastrar Candidato \n")
	print(" 2 - Cadastrar Eleitor   \n")
	print(" 3 - Ver Eleitores       \n")
	print(" 4 - Ver Candidatos      \n")
	print(" 5 - Votar               \n")
	print(" 6 - Apuração de Votos   \n")
	print("-------------------------\n")

	op = int(input(""))

	if op == 0:
		print('Fim')

	elif op == 1:

		print("fdsf")

	elif op == 2:
		qtdEleitores = int(input("Quantidade de eleitores para cadastrar: "))
		for a in range(qtdEleitores):
			nomeEleitor = input("Nome do eleitor: ")
			id_eleitor = input("ID do eleitor: ")
			eleitor = eleitores()
			eleitor.cadastrar_eleitor(nome = nomeEleitor, id_eleitor = id_eleitor)

	elif op == 3:
		eleitor.exibir_eleitor()

	elif op == 4:
		exibir_candidatos()

	elif op == 5:
		votacao()

	elif op == 6:
		apuracao_votos()

	else:
		print('Opção Inválida')

candidato = candidatos()
candidato.cadastrar_candidato(nome = 'Lucas', numeroVoto = 12)

candidato.votar()

candidato.exibir_candidato()

branco = opcaoVoto()
branco.cadastro_NB(2)
branco.votar()
branco.exibir_NB()

nulo = opcaoVoto()
nulo.cadastro_NB(1)
nulo.votar()
nulo.exibir_NB()
