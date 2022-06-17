# User inputs:
a = float(input('Enter first side: '))
b = float(input('Enter second side: '))
c = float(input('Enter third side: '))

# Calculations
s = (a+b+c) / 2
Area= (s*(s-a)*(s-b)*(s-c))**(1/2)

# Checking whether Triangle can be formed. If so, displaying Area
if a+b>c and b+c>a and a+c>b:
    print('Area of triangle is:', Area)
else:
    print('Triangle Not Possible')
