# DESAFIO
# Fechar possiveis brechas pra erro.
# Adicionar o nome ao eleitor.
# Adicionar um menu se a pessoa quer cadastrar um candidato ou eleitor
# No menu tbm tem a opção de votar ou ver apuração de votos
# Dica coloque um campo no eleitor pra poder indicar quem vai votar

from random import *

opcaoVoto = [{
            "nome": "Voto branco",
            "qtdVotos": 0,
            "NumeroVoto": "b",
        },
        {
            "nome": "Voto nulo",
            "qtdVotos": 0,
            "NumeroVoto": "n",
        }]

eleitores = []
candidatos = []
qtdCandidatos = 0
qtdEleitores = 0


def menu():

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
            
            qtdCandidatos = int(input("Quantidade de canditos pra eleição: "))
            cadastro_candidatos(qtdCandidatos)

        elif op == 2:
            qtdEleitores = int(input("Quantidade de eleitores para votar: "))
            cadastro_eleitor(qtdEleitores)

        elif op == 3:
            exibir_eleitores()

        elif op == 4:
            exibir_candidatos()

        elif op == 5:
            votacao()

        elif op == 6:
            apuracao_votos()

        else:
            print('Opção Inválida')


    def eleicao():
        qtdCandidatos = int(
        input("Quantidade de candidatos pra eleição: "))
        cadastro_candidados(qtdCandidatos)

        if qtdCandidatos < 1:
            print("Opção Inválida")

        else:

            print("------------------------\n")
            qtdEleitores = int(input("Quantidade de eleitores para votar: "))
            print("------------------------\n")
            cadastro_eleitor(qtdEleitores)

        for e in range(eleitores):
            cont = 1
            print("Eleitor - %s" % (e+1))
            for o in opcaoVoto:
                print("Pra votar '%s' digite: %s" % (o['nome'], cont))
                cont += 1

            voto = int(input("Digite sua opçao: "))
            opcaoVoto[voto-1]['qtdVotos'] += 1
            print("------------------------\n")

        for c in opcaoVoto:
            print("------------------------\n")
            print("Opção: %s" % c['nome'])
            print("Total de votos: %s" % c['qtdVotos'])
            print("------------------------\n")

def votacao():

    for cont in candidatos:
        print("%s | Número para votar: %s" % (cont["nome"], cont["NumeroVoto"])) 
        

    for i in opcaoVoto:
        print("%s | Número para votar: %s" % (i["nome"], i["NumeroVoto"]))

    eleitor = int (input("ID Eleitor: "))

    aux = verifica_id(eleitor)    
    while aux != False:
        try:
            print("Opção não encontrada digite novamente")
            eleitor = int(input("ID Eleitor: "))            
        except:
            print("Id invalido, insira outro")

        aux = verifica_id(eleitor)


    voto = input("Digite seu voto: ")
    if not voto == 'n' and not voto == 'b':
        voto = int(voto)
        aux = verifica_nv(voto)
          
        while aux != False:
            try:
                print("Opção não encontrada digite novamente")
                voto = int(input("Digite seu voto: "))
                 
            except:
                print("Id invalido, insira outro")
            aux = verifica_nv(voto)
            

    if voto == 'b' or voto == 'n':
        for op in opcaoVoto:
            if op['NumeroVoto'] == voto:
                op['qtdVotos'] += 1
    else:
        for op in candidatos:
            if op['NumeroVoto'] == voto:
                op['qtdVotos'] += 1

    print("Voto Computado")

def cadastro_candidatos(qtdCandidatos):

    for cont in range(qtdCandidatos):
        nome = input("Nome do candidato: ")
        nv = int(input("Número Voto: "))
        print("------------------------\n") 

        inexistente = False

        while inexistente != True:
            inexistente = verifica_nv(nv)
            if inexistente == False:
                print("Número Existente")
                nv = int(input("Número Voto: "))

        candidato = {
            "nome": nome,
            "qtdVotos": 0,
            "NumeroVoto": nv,
        }
        candidatos.append(candidato)

def cadastro_eleitor(qtdEleitores):
    for cont in range (qtdEleitores):
        nome = input("Nome do Eleitor: ")
        print("----------------------\n")
        id_eleitor = randint (0, 1000)

        inexistente = False

        while inexistente != True:
            inexistente = verifica_id(id_eleitor)
            if inexistente == False:
                id_eleitor = randint (0, 1000)

        eleitor = {
        "nome": nome,
        "id": id_eleitor,
        }
        eleitores.append(eleitor)

def verifica_id(id_eleitor):
    inexistente = True
    for e in eleitores:
        if id_eleitor == e["id"]:
            inexistente = False
            break 

        else:
            inexistente = True

    return inexistente  

def verifica_nv(nv):
    inexistente = True
    for i in candidatos:

        if nv == i["NumeroVoto"]:
        
            inexistente = False
            break

        else:
            inexistente = True

    return inexistente

def exibir_eleitores():
    for cont in eleitores:
        print("Nome: %s" % cont["nome"])
        print("ID: %s" % cont["id"])  

def exibir_candidatos():
    for cont in candidatos:
        print("Nome: %s" % cont["nome"]) 
        print("Votos: %s" % cont["qtdVotos"])  

def apuracao_votos():
    for cont in opcaoVoto:
        print("Voto %s Nº Votos: %s" % (cont["nome"], cont["qtdVotos"]))

    for i in candidatos:
        print("Candidato(a) %s Nº Votos: %s" % (i["nome"], i["qtdVotos"]))

    votoBranco = opcaoVoto[0]['qtdVotos']
    votoNulo = opcaoVoto[1]['qtdVotos']

    qtdEleitores = len(eleitores)

    votoBranco = (votoBranco * 100) / qtdEleitores
    print("Percentual de votos em branco: %0.2f" % votoBranco)


    votoNulo = (votoNulo * 100) / qtdEleitores
    print("Percentual de votos nulos: %0.2f" % votoNulo)
