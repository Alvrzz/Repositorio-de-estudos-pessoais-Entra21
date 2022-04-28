from random import randint
from time import sleep
escolha = randint(1,6) 
print('--'*30)
print('Tente acertar um número entre "1" e "6"')
print('--'*30)
j = int(input('Sua aposta: '))
print('processando...')
sleep(2)
if j == escolha:
    print('--'*30)
    print(f'Parabens você escolheu o número certo! "{escolha}"')
    print('--'*30)
else:
    print('--'*30)
    print(f'Você errou, mais sorte na próxima!\nO numero escolhido foi "{escolha}".')
    print('--'*30)
