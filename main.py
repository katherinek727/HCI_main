print('FIU')

first_name = 'Greg'
last_name = 'Reis'

print(first_name + ' ' + last_name)

university = 'FIU'
year = '2014'

print('{} has been working at {} since {}'.format(first_name,university,year))

a = 10
b = 3
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a**b)
print(a//b)
print(a%b)

import math

print(math.sqrt(16))
print(math.factorial(5))

print(type(False), True)

for i in range(10):
    print(i)

professor = ['greg', 'richard', 'kianoosh', 'debra', 'agoritsa']
print(professor, type(professor), len(professor))
print(professor[1].title())
print(professor[-1])
print(professor[1:3]) # accessing element 1 and 2
print(professor[:3])

professor.append('waqas')
print(professor)
professor.insert(2,'jason')
print(professor)
professor.extend(['mark', 'leonardo', 'patricia'])
print(professor)
professor.remove('richard')
professor.pop(2)
print(professor.index('agoritsa'))