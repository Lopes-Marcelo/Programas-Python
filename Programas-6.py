#Entrada de valores
print('='*18)
print('Exercício 2: idade')
print('='*18)
nome = input ("Como se chama? ")
ano = eval (input ("Nasceu em que ano? "))
mes = eval (input ("Nasceu em que mês? "))
dia = eval (input ("Nasceu em que dia? "))
ano_atual = eval (input ("Ano atual? "))
mes_atual = eval (input ("Mês atual? "))
dia_atual = eval (input ("Dia atual? "))
dataNasc = datetime.date(ano, mes, dia)
dataAtual = datetime.date(ano_atual, mes_atual, dia_atual)

#diferença retorna em timedelta
diferenca = (dataAtual - dataNasc)
#Cálculos e Resultados
rslt = (diferenca.days / 365.25)
#ano_atual-ano

if (dia == dia_atual and mes == mes_atual):
    print ("O %s tem %d anos!" %(nome, rslt))
else:
    ((dia > dia_atual and mes == mes_atual) or mes < mes_atual)
    print ("O %s tem %d anos!" %(nome, rslt))
