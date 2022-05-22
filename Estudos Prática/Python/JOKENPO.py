from random import randint
from time import sleep
itens = 'Pedra','Papel','Tesoura'
pc = randint(0,2)
computador = 'O computador venceu com'
jogador = 'O jogador ganhou!!\nCom:'
print('--'*31)
player = (input(
'''JOKENPO
[ 0 ]Pedra
[ 1 ]Papel
[ 2 ]Tesoura
Sua escolha: '''))
print('-='*31) 
if player:
    player = int(player)
    print('JO')
    sleep(1)
    print('KEN')
    sleep(1)
    print('PO!')
    sleep(1)
    print('-='*30)
    if pc == player or player == pc: #empate
        print(f'Empatou!!!\nComputador jogou: {itens[pc]}\nE você jogou: {itens[player]}!')

    elif pc == 0: #computador jogou pedra
        if player == 1:
            print(f'{jogador} {itens[player]}!\nEnquanto o computador jogou: {itens[pc]}!')
        elif player == 2:
            print(f'{computador} {itens[pc]}!!')

    elif pc == 1: #computador jogou papel
        if player == 0:
            print(f'{computador} {itens[pc]}!! ')
        elif player == 2:
            print(f'{jogador} {itens[player]}!\nEnquanto o computador jogou: {itens[pc]}!')

    elif pc == 2: #computador jogou tesoura~
        if player == 0:
            print(f'{jogador} {itens[player]}!\nEnquanto o computador jogou: {itens[pc]}!')
        elif player == 1:
            print(f'{computador} {itens[pc]}')
else:   
    print('Digite corretamente sua opção.')    

print('-='*31)





