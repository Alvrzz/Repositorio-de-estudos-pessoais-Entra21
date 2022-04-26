def contador_letras(lista_palavras):
    contador = []
    for x in lista_palavras:
        quantidade= len(x)
        contador.append(quantidade)
    return contador

if __name__ == '__main__': 
    lista = ['palavrass', 'palavrass'] #<----COLOQUE AQUI A PALAVRA
    print('--'*30)
    print('Total de letras:', contador_letras(lista))
    print('--'*30)
