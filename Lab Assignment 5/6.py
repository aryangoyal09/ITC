# Input ranges:
lower_range = int(input('Enter lower range: '))
upper_range = int(input('Enter upper range: '))

# To ensure that no errors are there for negative, 0 or 1 lower_range:
if lower_range<2:
    lower_range=2

for i in range(lower_range, upper_range+1):
    for j in range(2,i):
        if (i%j)==0:
            break 
    else:
        print(i)
