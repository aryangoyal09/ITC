# Asking user for Inputs:
lower_range = int(input('Enter lower range: '))
upper_range = int(input('Enter upper range: '))
n = int(input('Enter number to check for: '))

numbers=''

for i in range(lower_range,upper_range+1):
    if i%n == 0:
        numbers = numbers + ', ' + str(i)

# We are slicing the answer string because there's an additional ", " at the start
print('The numbers are:', numbers[2::])
