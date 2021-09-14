#! /usr/bin/python3
#jeito 1: usando for para contar vogais em um texto
vogais= ['a', 'e', 'i', 'o', 'u']
poema = """No meio do caminho tinha uma pedra
tinha uma pedra no meio do caminho
tinha uma pedra
no meio do caminho tinha uma pedra.
Nunca me esquecerei desse acontecimento
na vida de minhas retinas tão fatigadas.
Nunca me esquecerei que no meio do caminho
tinha uma pedra
tinha uma pedra no meio do caminho
no meio do caminho tinha uma pedra."""

contador= 0
for letra in poema: #comando para verificar cada caractere contido no texto "poema"
    if letra in vogais: 
        contador = contador + 1
print(contador)

#jeito 2: utilizando while

contador = 0
index = 0 #index de inicialização 
while (index < len(poema)):
    letra = poema[index] #guarda cada caractere contido no texto "poema"
    if letra in 'aeiou': #verifica e conta se "aeiou" está contido na variável "letra"
        contador += 1
    index += 1 #atualização do index para cada rodada do while 
print(contador)

