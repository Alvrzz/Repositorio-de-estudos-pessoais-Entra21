from random import randint 
from time import sleep
itens = 'Pedra','Papel','Tesoura' 
pc = randint(0,2)
computador = 'O computador venceu!!\nCom:'
jogador = 'O jogador ganhou!!\nCom:'
print('=-'*31)
player = (input(
'''     JOKENPO
[ 0 ] Pedra
[ 1 ] Papel
[ 2 ] Tesoura
Sua escolha: ''')).strip()

print('-='*31) 

try:
    if player == '0' or  player =='1' or  player == '2':
        player = int(player)
        print(f'Você escolheu {itens[player]}!')
        sleep(1)
        print('E vamos ao jogo!!!\n')
        sleep(2)
        print('JO..\n')
        sleep(1)
        print('KEN..\n')
        sleep(1)
        print('PO!\n')
        sleep(1)
        print('-='*30)
        if pc == player or player == pc: #empate
            print(f'Empatou!!!\nComputador jogou: {itens[pc]}\nE você jogou: {itens[player]}!')

        elif pc == 0: 
            if player == 1:
                print(f'{jogador} {itens[player]}!\nEnquanto o computador jogou: {itens[pc]}!')
            elif player == 2:
                print(f'{computador} {itens[pc]}!\nEnquanto o jogador jogou: {itens[player]}!')

        elif pc == 1:
            if player == 0:
                print(f'{computador} {itens[pc]}!\nEnquanto o jogador jogou: {itens[player]} ')
            elif player == 2:
                print(f'{jogador} {itens[player]}!\nEnquanto o computador jogou: {itens[pc]}!')

        elif pc == 2: 
            if player == 0:
                print(f'{jogador} {itens[player]}!\nEnquanto o computador jogou: {itens[pc]}!')
            elif player == 1:
                print(f'{computador} {itens[pc]}!\nEnquanto o jogador jogou: {itens[player]}!')
    else:
        print('Digite corretamente sua opção.')                
except:
    print('Digite corretamente sua opção.')


print('-='*31)





