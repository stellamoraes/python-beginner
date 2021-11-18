#Python Exercise: Make a simple calculator

num1= 0 
num2= 0

def addition(num1, num2):
    return num1 + num2
       
def subtraction(num1, num2):
    return num1 - num2 
      
def multiplication(num1, num2): 
    return num1 * num2

def division(num1, num2):
    return num1 / num2

while (num1 >= 0)  and (num2 >= 0): #loop limit
    num1= int(input('Insert a number:'))
    num2= int(input('Insert another number:'))
    operation= input('Insert the basic math operation (+,-, *, /):' )
    if operation == '+':
        print (addition(num1, num2)) 
    elif operation == '-':
        print (subtraction(num1, num2))     
    elif operation == '*':
        print (multiplication(num1, num2))   
    elif operation == '/':
        print (division(num1, num2))
    else:
        print('Invalid Operation.')       
       

