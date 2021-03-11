import math

def compras():

	morangos = input('Digite a quantidade de morangos: \n')
	macas = input('Digite a quantidade de maçãs: \n')


	morangos = int(morangos)
	macas = int(macas)

	if morangos <= 5:
		kg_morangos = morangos * 2.5
		print('Valor a ser pago: ', kg_morangos)

	else: 
		kg_morangos = morangos * 2.2	
		print('Valor a ser pago: ', kg_morangos)


	if macas <= 5:
		kg_macas = macas * 1.8
		print('Valor a ser pago: ', kg_macas)

	else:
		kg_macas = macas * 1.5
		print('Valor a ser pago: ', kg_macas)

	preco_total = kg_morangos + kg_macas
	peso_total = morangos + macas

	if peso_total > 8 or preco_total > 25:
		preco_total = preco_total * 0.9
		print('Valor da compra: ', preco_total)