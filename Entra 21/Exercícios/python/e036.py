#e036.py

frase = str(input('Digite uma palavra ou frase:')).strip().upper()
# print(frase)

palavras = frase.split()
# print(palavras)


caracteres = ''.join(palavras)
# print(caracteres)

fraseinvertida = ''

# range(start,stop,setep)
# range(inicio, fim, passo)
print(range(len(caracteres)-1,-1,-1))
for i in range(len(caracteres)-1,-1,-1):
    fraseinvertida += caracteres[i]
    print(f'{i} Cr: {caracteres[i]}')

    
print(caracteres,fraseinvertida)
if fraseinvertida == caracteres:
    print('É um palindromo!!!')
else:
    print('não é')


