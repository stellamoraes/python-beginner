#! /usr/bin/python3
count= int(input('Quantidade de donuts:'))

def donuts (count):
    returno = ""
    if count < 10:
        returno = "Número de donuts: <{}>".format(count)
    else:
        returno = "Número de donuts: many"        
    return returno
print (donuts(count))