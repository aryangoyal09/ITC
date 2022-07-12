def panagram(line):
    alphabet='abcdefghijklmnopqrstuvwxyz'

    for i in alphabet:
        if i in line.lower():
            continue
        print('Not a panagram')
        break
    else:
        print('Panagram!')

# Asking user for input line
line = str(input('Enter string to check for: '))
panagram(line)
