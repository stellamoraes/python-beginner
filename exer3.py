palavra= input('Insira uma palavra:')

def fix_start(palavra): 
    letra_um= palavra[0]
    resto_palavra= palavra[1:]
    nova_palavra= resto_palavra.replace(palavra[0],'*') 
    return (letra_um) + (nova_palavra)
fix_start(palavra)
print (fix_start(palavra))