num = int(input('Digite o numero: '))
razao = int(input('Razão: '))

for c in range(1,10):
    num += razao
    print(f' {num} ',end='->')