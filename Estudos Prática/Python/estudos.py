n = int(input('Quantos dias rodados: '))
b = float(input('Quantos km rodados: '))

v1 = n * 60
v2 = b * 0.15

print(f'total a pagar: R${v1 + v2:.2f}')