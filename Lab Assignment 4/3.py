import random

for i in range(1,11):
    a=random.randint(1,10)
    b=random.randint(1,10)
    print('Question', i, ':', a, '*', b, '= ??')
    answer=int(input('Enter answer: '))
    if answer==a*b:
        print('Right!')
    elif answer!=a*b:
        print('Wrong. The answer is', a*b)
    print()
