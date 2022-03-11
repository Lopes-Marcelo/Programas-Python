from time import sleep

print(' = ' * 15)
print('           Calculadora         ')
print(' = ' * 15)
print()

#Entrada De Pergunta

print('Olá, bem vindo à calculadora!')
print()
nome = input('Qual é o seu nome? ')
print()

pergunta_inicial = str(input ('Gostaria de fazer um cálculo? '))
print()

if pergunta_inicial == "sim" :
    print('Maravilha,' , nome ,'!!!')
    print()
    
    pergunta_2 = str(input('Quer envolver quantos números em seus cálculos? 1, 2 ou 3? '))
    print()
    
    
    if pergunta_2 == "1" :

#Entrada De Valores 1       
        
        numero_1 = int(input ('Informe um número: '))
        print()
        
        quad1 = numero_1**2
        cub1 = numero_1**3
        
#Cálculos e Resultados Com Um Número
        
        sleep (1)
        print( numero_1,'²' , '=' , quad1 )
        sleep (1)
        print( numero_1,'³' , '=' , cub1)
        print()

        print('=' * 40)
        print(' Volte sempre ',nome,'!')
        print('=' * 40)
        
        
    elif pergunta_2 == "2" :
        
#Entrada De Valores 2        
        
        numero_1 = int(input ('Informe um número: '))
        numero_2 = int(input ('Informe outro número: '))
        print ()

        soma = numero_1 + numero_2
        subtracao = numero_1 - numero_2
        multi = numero_1 * numero_2
        divi = numero_1/numero_2
        quad1 = numero_1**2
        quad2 = numero_2**2
        cub1 = numero_1**3
        cub2 = numero_2**3

#Cálculos e Resultados Com Dois Números
    
        sleep (1)
        print( numero_1 , '+' , numero_2 , '=' , soma )
        sleep (1)
        print( numero_1 , '-' , numero_2 , '=' , subtracao)
        sleep (1)
        print( numero_1 , 'x' , numero_2 , '=' , multi)
        sleep (1)
        print( numero_1 , '/' , numero_2 , '=' , divi)
        sleep (1)
        print( numero_1,'²' , '=' , quad1 )
        sleep (1)
        print( numero_2,'²' , '=' , quad2)
        sleep (1)
        print( numero_1,'³' , '=' , cub1)
        sleep (1)
        print( numero_2,'³' , '=' , cub2)
        sleep (1)
        print()

        print('=' * 40)
        print(' Volte sempre ',nome,'!')
        print('=' * 40)
        
    elif pergunta_2 == "3" :

#Entrada De Valores 3        
        
        numero_1 = int(input ('Informe um número: '))
        numero_2 = int(input ('Informe outro número: '))
        numero_3 = int(input ('Informe mais um número: '))
        print()
        
        soma = numero_1 + numero_2 + numero_3
        multi = numero_1 * numero_2 * numero_3
        quad1 = numero_1**2
        quad2 = numero_2**2
        quad3 = numero_3**2
        cub1 = numero_1**3
        cub2 = numero_2**3
        cub3 = numero_3**3
        
#Cálculos e Resultados Com Três Números
        
        sleep (1)
        print( numero_1 , '+' , numero_2 , '+' , numero_3 , '=' , soma )
        sleep (1)
        print( numero_1 , 'x' , numero_2 , 'x' , numero_3 , '=' , multi)
        sleep (1)
        print( numero_1,'²' , '=' , quad1)
        sleep (1)
        print( numero_2,'²' , '=' , quad2)
        sleep (1)
        print( numero_3,'²' , '=' , quad3)
        sleep (1)
        print( numero_1,'³' , '=' , cub1)
        sleep (1)
        print( numero_2,'³' , '=' , cub2)
        sleep (1)
        print( numero_3,'³' , '=' , cub3)
        print()

        print('=' * 40)
        print(' Volte sempre ',nome,'!')
        print('=' * 40)
    
    else:
        
        print()
        sleep (1)
        print('Não foi possível entender sua resposta' ,nome,', execute o programa novamente!')
        print()
        sleep (1)
        print('=' * 40)
        print('          Volte sempre!')
        print('=' * 40)

elif pergunta_inicial == "nao" :
    print()
    sleep (1)
    print('Tudo bem' , nome, ', quem sabe na próxima!')
    print()
    sleep (1)
    print('=' * 40)
    print('  Volte sempre!')
    print('=' * 40)

else:
    print()
    sleep(1)
    print('Não foi possível entender sua resposta' ,nome,', execute o programa novamente!')
    print()
    sleep (1)
    print('=' * 40)
    print('          Volte sempre!')
    print('=' * 40)

#Fazer o looping
    #while pfinal != sair
    
#Poder escolher a operação 