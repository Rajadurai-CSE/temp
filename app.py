from feature1 import addition
from feature2 import subtraction
print('simple calculator')
print('Enter two numbers')
a = int(input('Enter number1:'))
b = int(input('Enter number2:'))
print('Enter 1 for Addition and 2 for subtraction')
c = int(input('Enter choice:'))

if c==1:
  print(addition(a,b))
else:
  print(subtraction(a,b))