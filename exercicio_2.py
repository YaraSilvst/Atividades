def nome_pessoas(nome_completo):

	nome_formatado =[nome.capitalize() for nome in nome_completo.split()]
	
	resultado = ' '.join(nome_formatado)
	resultado = resultado.replace(' Da ', ' da ').replace(' De ', ' de ')
 

	return resultado 

	



	

