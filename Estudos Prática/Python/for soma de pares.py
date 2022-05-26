soma = 0
conta = 0

for c in range(1,7):
    num = int(input(f'Digite {c} numero: '))
    if num % 2 == 0:
        soma += num
        conta += 1
   
print(f'A soma dos {conta} pares foi de {soma} ')