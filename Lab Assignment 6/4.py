line = str(input('Enter string to check for: '))
alphabet='abcdefghijklmnopqrstuvwxyz'

for i in alphabet:
    if i in line.lower():
        continue
    print('Not a panagram')
    break
else:
    print('Panagram!')
