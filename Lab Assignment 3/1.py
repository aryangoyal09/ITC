num = int(input('Enter number: '))

#Supposing we want to do this without bin() :
a=''
if num == 0:
    print('Binary of number =', 0)
else:
    while num !=0:
        a = str(num % 2) + a
        num = num//2
    print('Binary of number =', a)
