a = 5
b = 4
soma = a + b
quadrado = soma**2

from time import sleep

print ('==' * 15)
print ('  -=     Calculadora     =-')
print ('==' * 15)

if (soma==9): 
    print ("Sim")
    for n in range (2):
        print ("Deu bom")
else:
    print ("Não")
    for n in range (2):
        print ("Deu Ruim") 
sleep(2)    
if quadrado==81:
    print ("sim")
    for n in range (3):
        print ("deu bom")
else: 
    print ("não")
    for n in range (3): 
        print ("deu ruim")
sleep(2)
