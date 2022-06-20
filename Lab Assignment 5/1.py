# Input line:
line = str(input('Enter string here: '))

reverse = ''

for i in line:
    reverse = i + reverse
print(reverse)
