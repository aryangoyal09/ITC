# Input line:
line = str(input('Enter string here: '))
reverse = line[::-1]

# As seen in the example "Nurses run", the program should ignore whitespaces and capitals
if line.lower().replace(' ', '') == reverse.lower().replace(' ', ''):
    print('Palindrome!')
else:
    print('Not a palindrome')
