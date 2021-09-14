#jeito 1: código extenso 
salario= int(input('Insira o salário para o calculo do reajuste: '))
if salario <= 280:
    aumento = salario*20/100
    novo_salario= salario + aumento
    print('Seu salário atual é: ', salario)
    print('Seu percental de aumento foi de 20%')
    print('Seu aumento salarial foi de: ', aumento)
    print('Seu novo salário é:', novo_salario)

elif (salario > 280) and (salario < 700):
    aumento = salario*15/100
    novo_salario= salario + aumento
    print('Seu salário atual é: ', salario)
    print('Seu percental de aumento foi de 15%')
    print('Seu aumento salarial foi de: ', aumento)
    print('Seu novo salário é:', novo_salario)
elif (salario > 700) and (salario < 1500):
    aumento = salario*10/100
    novo_salario= salario + aumento
    print('Seu salário atual é: ', salario)
    print('Seu percental de aumento foi de 10%')
    print('Seu aumento salarial foi de: ', aumento)
    print('Seu novo salário é:', novo_salario )
else:
    aumento = salario*5/100
    novo_salario= salario + aumento
    print('Seu salário atual é: ', salario)
    print('Seu percental de aumento foi de 5%')
    print('Seu aumento salarial foi de: ', aumento)
    print('Seu novo salário é:', novo_salario )

#jeito 2: código limpo e reduzido
salario= int(input('Insira o salário para o calculo do reajuste: '))
if salario <= 280:
    perc_aumento= 20
elif (salario > 280) and (salario < 700):
    perc_aumento= 15
elif (salario > 700) and (salario < 1500):
    perc_aumento= 10
else:
    perc_aumento= 5

aumento = salario*perc_aumento/100
novo_salario= salario + aumento
print('Seu salário atual é: ', salario)
print('Seu percental de aumento foi de', perc_aumento, '%'.)
print('Seu aumento salarial foi de: ', aumento)
print('Seu novo salário é:', novo_salario )    