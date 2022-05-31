print('--'*30)
print('O número é IMPAR ou PAR?')
print('--'*30)
num = int(input('Digite o número: '))
r = num % 2
if r == 0:
    print('--'*30)
    print(f'{num} é PAR')
    print('--'*30)
else:
    print('--'*30)
    print(f'{num} é IMPAR.')
    print('--'*30)