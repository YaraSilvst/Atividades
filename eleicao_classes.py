from random import *

eleitores_lista = []
candidatos_lista = []

def verifica_id(id_eleitor):
	inexistente = True
	for e in eleitores_lista:
		if id_eleitor == e.id_eleitor:
			inexistente = False
			break 

		else:
			inexistente = True

	return inexistente 


class eleitores(): 

	def __init__(self):
		self.nome = ''
		self.id_eleitor = 0

	def cadastrar_eleitor(self, nome, id_eleitor):
		inexistente = False

		while inexistente != True:
			inexistente = verifica_id(self.id_eleitor)
			if inexistente == False:
				print("hihih")

		self.nome = nome
		self.id_eleitor = id_eleitor

		eleitores_lista.append(self)
		print(eleitores_lista)

	def exibir_eleitor(self):
		for a in eleitores_lista:
			print('Nome: %s' %(a.nome))
			print('ID: %s' %(a.id_eleitor))

class candidatos():

	def __init__(self):
		self.nome = ''
		self.numeroVoto = ''
		self.qtdVotos = 0

	def cadastrar_candidato(self, nome, numeroVoto):
		self.nome = nome
		self.numeroVoto = numeroVoto

		candidatos_lista.append(self)

	def exibir_candidato(self):
		print('Nome: %s' %(self.nome))
		print('Número Voto: %s' %(self.numeroVoto))

	def votar(self):
		self.qtdVotos +=1

class opcaoVoto():

	def __init__(self):
		self.qtdVotos = 0
		self.numeroVoto = ''

	def cadastro_NB(self, numeroVoto):
		self.numeroVoto = numeroVoto

	def exibir_NB(self):
		print(self.numeroVoto)
		print(self.qtdVotos)


	def votar(self):
		self.qtdVotos +=1



