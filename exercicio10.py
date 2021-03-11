def soma():

	try:
		n1 = int(input("Digite o primeiro número: "))
		n2 = int(input("Digite o segundo número: "))
		n3 = n1 + n2
		print("---------")
		print("Soma:", n3)
		print("---------")

	except:
		print("Inválido")


def subtracao():

	try:
		n1 = int(input("Digite o primeiro número: "))
		n2 = int(input("Digite o segundo número: "))
		n3 = n1 - n2
		print("--------------")
		print("Subtração:", n3)
		print("--------------")

	except:
		print("Inválido")

def multiplicacao():

	try:
		n1 = int(input("Digite o primeiro número: "))
		n2 = int(input("Digite o segundo número: "))
		n3 = n1 * n2
		print("------------------")
		print("Multiplicação:", n3)
		print("------------------")

	except:
		print("Inválido")

def divisao():

	try:
		n1 = int(input("Digite o primeiro número: "))
		n2 = int(input("Digite o segundo número: "))
		n3 = n1 / n2
		print("------------")
		print("Divisão:", n3)
		print("------------")

	except:
		print("Inválido")

def menu():

	op = 10


	while op != 0:
		print(" ------------------------ \n")
		print("|       CALCULADORA      |\n")
		print("|------------------------|\n")
		print("|1 - Somar               |\n")
		print("|2 - Subtrair            |\n")
		print("|3 - Multiplicar         |\n")
		print("|4 - Dividir             |\n")
		print(" ------------------------ \n")


		op = int(input(""))

		if op == 1:
			aux = input("Aperte Enter")
			soma()

		elif op == 2:
			aux = input("Aperte Enter")
			subtracao()

		elif op == 3:
			aux = input("Aperte Enter")
			multiplicacao()

		elif op == 4:
			aux = input("Aperte Enter")
			divisao()

		else:
			print("Opção Inválida")


		



