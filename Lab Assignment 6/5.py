# Taking and splitting the input by hyphen
list = str(input('Enter words separated by hyphen: ')).split('-')
list.sort()
output = ''

for i in list:
    output = output + '-' + i

# We need to ignore the first hyphen
print(output[1::])
