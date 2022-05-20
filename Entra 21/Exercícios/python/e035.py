numero = int(input('Digite um número:'))
divisoes = 0 

# range(start, stop, step)
for i in range(1,numero + 1):
    print(f'i ->{i} mod: {numero%i}')
    if numero %i == 0:
        divisoes += 1
        # print(f'i:{i}, numero: {numero%i}')        
if divisoes == 2:
    print(f'{numero} é primo!!!!')
    print(f'{numero} é divisivel por um ou por {numero}')
else:
    print(f'{numero} NÃO é primo')
    print(f'{numero} é divisível {divisoes} vezes')