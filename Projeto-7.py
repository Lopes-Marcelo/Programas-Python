from random import randint
from time import sleep
from operator import itemgetter

atravessar = {'rua A': randint(1,2),
              'rua B': randint(1,2),
              'rua C': randint(1,2),
              'rua D': randint(1,2),
              'rua E': randint(1,2),
              'rua F': randint(1,2)}

resultado = list()

print ('==' * 16)
print ('SERÁ QUE DÁ PARA ATRAVESSAR A RUA?')
print ('==' * 16)
print()

print ('São 6 vias, 3 para cada sentido. Será que está vindo carro?')
print()

for k, v in atravessar.items ():
    
    
    print (f'{k} {v} está vindo carro.')
   
sleep(1)
