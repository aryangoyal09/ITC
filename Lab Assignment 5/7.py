numbers = ''

for i in range(1,501):
    if i%7==0 and i%11==0:
        numbers= numbers + ', ' + str(i)

# We are slicing the answer string because there's an additional ", " at the start
print('numbers which are multiple of 7 and divisible by 11:', '\n', numbers[2::])
