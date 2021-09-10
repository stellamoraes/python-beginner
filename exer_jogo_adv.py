"""
    JOGO ADIVINHA NUMERO

    O COMPUTADOR DEVE GERAR UM NUMERO ALEATORIO ENTRE 1 E 10
    O COMPTADOR DEVE PERGNTAR AO JOGADOR O SEU PALPITE
    SE O PALPITE FOR MAIOR, O JOGO DEVE PEDIR PRA ELE INFORMAR UM NUMERO MENOR
    SE O PALPITE FOR MENOR, O JOGO DEVE PEDIR PRA ELE INFORMAR UM NUMERO MAIOR

    SE ELE ACERTAR TEM Q DAR OS PARABENS
    TEM Q MOSTRAR A QUANTIDADE DE PALPITES
    O JOGADOR TEM 8 TENTATIVAS 

    FROM RANDOM IMPORT RANDINT
    NUMARO_SECRETO = RANDINT(1, 10)
"""
from random import randint 
n_sorteado= randint(1,10)
palpite= -1
tentativa=0
fim= 8

while True:
    palpite = int(input ('Qual o seu palpite?'))
    tentativa = tentativa + 1 
    if (palpite > n_sorteado):
        print ('Tente um número menor.')
    elif (palpite < n_sorteado):
        print ('Tente um número maior')
    elif (palpite == n_sorteado):
        print ('Parabéns, você acertou!')
        break
print ('Você tentou ' + str(tentativa) + ' vez(es).')        
print('Jogo finalizado!')