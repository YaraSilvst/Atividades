def calculo_imc(peso, altura):
    try:
        imc = peso / (altura * altura)

    except:
        print('Valor Inválido')

    if imc < 16:
        print("Magreza Grave")

    elif imc > 16 and imc < 17:
        print('Magreza Moderada')

    elif imc > 17 and imc < 18.5:
        print('Magreza Leve')

    elif imc > 18.5 and imc < 25:
        print('Saudável')

    elif imc > 25 and imc < 30:
        print('Sobrepeso')

    elif imc > 30 and imc < 35:
        print('Obesidade Grau 1')

    elif imc > 35 and imc < 40:
        print('Obesidade Grau 2 (severa)')

    else:
        print('Obesidade Grau 3 (mórbida')
