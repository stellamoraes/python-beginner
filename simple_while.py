username= ''
password= ''

while username == password:
    username= input('Insert here your username: ')
    password= input('Insert your password: ')
    
    if username != password:
        print('Login successful.')
    else: 
        print('Username and password must be different.')    
