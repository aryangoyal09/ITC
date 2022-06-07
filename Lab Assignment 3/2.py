b = float(input('Enter first number: '))
a = input('Enter sign(+, -, *, / or q for quit): ')

# Supposing we want to do this without eval()
while (a!='q'):
    if a=='+':
        b = b + float(input('Next number: '))
    elif a == '-':
        b = b - float(input('Next number: '))
    elif a == '*':
        b = b * float(input('Next number: '))
    elif a == '/':
        b = b / float(input('Next number: '))
    else:
        print('Invalid operator, try again')
    a = input('Enter next sign(+, -, *, / or q for quit): ')

print(b)
