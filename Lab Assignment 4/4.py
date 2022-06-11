# Start from 1 and into a while loop:
a=1

while a<200:
    if (a%5 == 2) and (a%6 == 3) and (a%7 == 2):
        print('No. of Candies =',a)
    a+=1
