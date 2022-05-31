from random import randint
#FUNÇÃO QUE TORNA OS NÚMEROS ALEATORIAMENTE
from time import sleep
#FUNÇÃO QUE DA UM ATRASO NA RESPOSTA
from operator import itemgetter
jogadores= {'jogador 1' : randint(1,6),
        'jogador 2' : randint(1,6),  
        'jogador 3' : randint(1,6),
        'jogador 4' : randint(1,6),
        'jogador 5' : randint(1,6),
        'jogador 6' : randint(1,6)}
# DEFININDO OS JOGADORES
raking = list ()
print('Resultados:')
for k, v in jogadores.items():
    print(f'{k} tirou {v} no dado.')
    sleep(1)
ranking = sorted(jogadores.items(), key=itemgetter(1), reverse=True)
print('--'*25)
print('            *Ranking dos Jogadores*')
print('--'*25)
for i, v in enumerate (ranking):
    print(f'{i+1}º Lugar: {v[0]} com o número {v[1]}.')
    sleep(1)
    print('--'*18)

print('            *Fim de Jogo*')