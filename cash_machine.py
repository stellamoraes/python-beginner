#Python Exercise: Creating a cash machine with bank account (using a file with client data) 
#Check the json file "bank_account.json" 

import json
import time 

with open('bank_account.json', 'r') as info: 
    account_data= json.loads(info.read()) 

print ('Initializing the cash machine...')
time.sleep(2)
print ('User name: ', account_data["user"],'/ Account balance: ', account_data["balance"])

current_balance= int(account_data["balance"])
operation= int(input('Insert 1 to withdrawal or 2 to deposit: '))

if operation == 1:
    withdrawal_amount= int(input('Insert the amount to withdrawal: '))
    if withdrawal_amount > current_balance:
        print('Your balance account is not enough.')
    else:
        current_balance -= withdrawal_amount

elif operation == 2:
    deposit_amount= int(input('Insert the amount to deposit: '))
    current_balance += deposit_amount

else:
    print('Invalid Operation!')  
account_data["balance"] = current_balance  

with open('bank_account.json', 'w') as file:
    data_to_text= json.dumps(account_data) 
    file.write(data_to_text)

print('You current amount is: ', current_balance)  
print('You have finish the operation.')  