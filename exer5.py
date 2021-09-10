palavra= 'doing'
def verbing(palavra):
    if len(palavra) >= 3:  
        if palavra[-3:] == 'ing':
            return ((palavra) + 'ly')
        else:    
            return((palavra) + 'ing')
    else:   
        return palavra            
print (verbing(palavra))
