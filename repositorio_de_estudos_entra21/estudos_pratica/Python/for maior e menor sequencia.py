lista_completa = [ x for x in range(1,43)]
lista_pares = []
lista_impares = []

for c in lista_completa:
  if c % 2 == 0:
    lista_pares.append(c)
  else:
    lista_impares.append(c)

print(lista_impares)
print(lista_pares)