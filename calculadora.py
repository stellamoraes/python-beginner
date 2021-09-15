#desafio:criar uma calculadora
#o primeiro valor atribuído às variáveis devem estar contido dentro da condição do WHILE
num1= 0 
num2= 0
#definindo as operações realizadas pela calculadora
def adicao(num1, num2):
    return num1 + num2
       
def subtracao(num1, num2):
    return num1 - num2 
      
def multiplicacao(num1, num2): 
    return num1 * num2

def divisao(num1, num2):
    return num1 / num2

while (num1 >= 0)  and (num2 >= 0): #estabelecendoo limite de parada do looping
    num1= int(input('Digite um número:'))
    num2= int(input('Digite outro número:'))
    operacao= input('Que operação deseja realizar (+,-, *, /)?' )
    if operacao == '+':
        print (adicao(num1, num2)) #chamando a função da adição
    elif operacao == '-':
        print (subtracao(num1, num2))     
    elif operacao == '*':
        print (multiplicacao(num1, num2))   
    elif operacao == '/':
        print (divisao(num1, num2))
    else:
        print('Operação inválida.')       
       

