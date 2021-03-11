opcaoVoto = []
eleitores = 0
qtdCandidatos = 0

def menu():

    op = 10


    while op != 0:
        print("-------------------------\n")
        print("    DIGITE UMA OPÇÃO     \n")
        print("-------------------------\n")
        print(" 1 - Cadastrar Candidato \n")
        print(" 2 - Cadastrar Eleitor   \n")
        print(" 3 - Votar               \n")
        print(" 4 - Apuração de Votos   \n")
        print("-------------------------\n")

        op = int(input(""))

        if op == 0:
            print('Fim')

        elif op == 1:
            cadastro_candidatos()

        elif op == 2:
            cadastro_eleitor()

        elif op == 3:
            eleicao()

        elif op == 4:
            print('4')

        else:
            print('Opção Inválida')

def cadastro_candidatos():
	qtdCandidatos = int(input("Quantidade de Candidatos:"))

	for cont in range(qtdCandidatos):
        nome = input("Nome do candidato: ")
        print("------------------------\n")
        candidato = {
            "nome": nome,
            "qtdVotos": 0,
        }
        opcaoVoto.append(candidato)

def listar_candidatos():
	for o in opcaoVoto:
		print(o['nome'])

