# Input:
n = int(input('Enter number of rows: '))

a=0
Alphabet='ABCDEFGHIJKLMNOPQRSTUVWXYZ'

for i in range(1,n+1):
    for j in range (1,i+1):
        print(Alphabet[a%26], end='')
        a+=1
    print()
