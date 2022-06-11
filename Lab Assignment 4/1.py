# Input Marks:
Marks = float(input('Enter your Marks: '))

if Marks<25 :
    print('Your Grade is F')
elif 25<=Marks<45 :
    print('Your Grade is E')
elif 45<=Marks<50 :
    print('Your Grade is D')
elif 50<=Marks<60 :
    print('Your Grade is C')
elif 60<=Marks<80 :
    print('Your Grade is B')
elif Marks>=80 :
    print('Your Grade is A')
else:
    print('Invalid Marks')
