from random import shuffle
j1 = str(input('Digite primeiro nome: '))
j2 = str(input('Digite segundo nome: '))
jogador = str(input('Digite terceiro nome: '))
j4 = str(input('Digite quarto nome: '))
lista = [j1,j2,jogador,j4]
shuffle(lista)
print('=-'*30)
(print(lista))
print('=-'*30)