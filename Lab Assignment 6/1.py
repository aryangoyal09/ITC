n = int(input('Enter number: '))
sum_of_divisors = 0

# Calculating sum of divisors of the input number
for i in range(1, n+1):
    if n%i==0:
        sum_of_divisors = sum_of_divisors + i

if n==0:
    print('Number is not perfect')
elif n == sum_of_divisors/2:
    print('Number is perfect')
else:
    print('Number is not perfect')
