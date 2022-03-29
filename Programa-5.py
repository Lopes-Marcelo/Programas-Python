from random import randint
from time import sleep
from operator import itemgetter
jogo = {'jogador A': randint(1,6),
        'jogador B': randint(1,6),
        'jogador C': randint(1,6),
        'jogador D': randint(1,6),
        'jogador E': randint(1,6)}
ranking = list()
print ('==' * 15)
print ('    JOGO DE DADOS    ')
print ('==' * 15)
print ('Valores sorteados:')
for k, v in jogo.items ():
    print (f"{k} tirou {v} no dado.")
sleep(1)
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
print('-=' * 15)
print(' -== RANKING DOS JOGADORES ==-')
for i, v in enumerate(ranking):
    print(f'{i+1}ºlugar: {v[0]} com {v[1]}.')
    sleep(1)
