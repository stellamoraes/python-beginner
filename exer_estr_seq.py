'''
#tarefa 1
print ('Olá, mundo!')

#tarefa 2
n= input ('Insira um número:')
print ('O número informado foi ' + n)

#tarefa 3
a = int(input ('Insira um número:'))
b = int(input ('Insira um número:'))
print (a + b)

#tarefa 4
a= int(input('Insira a primeira nota:'))
b= int(input('Insira a segunda nota:'))
c= int(input('Insira a terceira nota:'))
d= int(input('Insira a quarta nota:'))
print ('A média das notas é: ', ((a + b + c + d)/ 4))

#tarefa 5
med_metro = int(input('Insira o valor  em (m) a ser convertido para (cm):'))
conversao= med_metro/100
print (conversao)

#tarefa 6
raio = int(input ('Raio do circunferência:'))
calculo= 3.14*raio**2 
print (calculo)

#tarefa 7
l= int(input('Lado do quadrado:'))
area= l**2 
db_area= area * 2
print (db_area)

#tarefa 8
salario_hora= int(input('Qual seu salário/h? '))
hora_trabalho= int(input('Quantas horas você trabalha por mês? '))
calculo_salario= salario_hora * hora_trabalho
print ('Você recebe {} reais por mês.'.format(calculo_salario))

#tarefa 9   
temp_fh= int(input('Insira a temperatura em graus Fahrenheit:'))
conv_celcius= 5 * ((temp_fh- 32)/ 9)
print ('Temperatura em °F convertida para °C: {}'.format(conv_celcius))

#tarefa 10
temp_celcius= int(input('Insira a temperatura em graus Celcius:'))
conv_fh= (temp_celcius + 1.8) + 32
print ('Temperatura em °C convertida para °F: {}'.format(conv_fh))
'''
#tarefa 11
n1= int(input ('Insira um número:'))
n2= int(input ('Insira um número:'))
n3= int(input('Insira um número:'))
conta1= (n1 * 2)  + (n2 / 2)
print (conta1)
conta2= (n1 * 3) + n3
print (conta2)
conta3= n3 ** 3
print (conta3)