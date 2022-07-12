# Defining function
def sorting(list):
    list.sort()
    output = ''

    for i in list:
        output = output + '-' + i

# We need to ignore the first hyphen
    print(output[1::])

# Input list
list = str(input('Enter words separated by hyphen: ')).split('-')
sorting(list)
