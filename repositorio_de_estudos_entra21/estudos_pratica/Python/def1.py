def dobra(lst): # dobro dos valores
    pos = 0
    while pos < len(lst): # cria a dobro dos valores
        lst[pos] *= 2
        pos += 1

valores = [3 , 4, 2, 5]

valores_dobrados = dobra(valores)
print(valores_dobrados)

#   ou
#dobra(valores)
#print(valores)




