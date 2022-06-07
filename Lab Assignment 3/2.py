num = float(input('Enter first number: '))
sign = input('Enter sign(+, -, *, / or q for quit): ')

# Supposing we want to do this without eval()
while (sign!='q'):
    if sign=='+':
        num = num + float(input('Next number: '))
    elif sign == '-':
        num = num - float(input('Next number: '))
    elif sign == '*':
        num = num * float(input('Next number: '))
    elif sign == '/':
        num = num / float(input('Next number: '))
    else:
        print('Invalid operator, try again')
    sign = input('Enter next sign(+, -, *, / or q for quit): ')

print(num)
