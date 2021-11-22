#Python Exercise: Create a code to calculate salary adjustment 
 
salary= int(input('Enter the salary to calculate the adjustment: '))
if salary <= 280:
    percent_increase= 20
elif (salary > 280) and (salary < 700):
    percent_increase= 15
elif (salary > 700) and (salary < 1500):
    percent_increase= 10
else:
    percent_increase= 5

percent_increase = salary*percent_increase/100
new_salary= salary + percent_increase

print('Old salary: ', salary)
print('Percentage adjustment', percent_increase, '%')
print('New salary:', new_salary )    