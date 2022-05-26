maior= 0
menor= 0

for p in range(1,6):
    peso = float(input(f'Peso da {p}ª pessoa: '))
    if p == 1:
        maior = p
        menor = p
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso

print(f'O menor doi de {menor} e o maior foi de {maior} ')