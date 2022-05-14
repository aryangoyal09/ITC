# 5. For any three lengths, there is a simple test to see if it is possible to form a triangle. If any of the three lengths is greater than the sum of the other two, then you cannot form a triangle. Otherwise, Enter three sides of a triangle, converts them to integers, and to check whether the given input lengths can form a triangle or not (Print : “Yes” or “No”).[Don’t use if else here].

# Inputting three sides of the triangle
a = float(input('Enter First side: '))
b = float(input('Enter Second side: '))
c = float(input('Enter Third side: '))

# Converting to integers as said in the Question
print('Convering Sides to Integer Values...\n')
a = int(a)
b = int(b)
c = int(c)

# Using Logical Operators as a Conditional Statement:
Condition = (a+b>c) and (b+c>a) and (a+c>b)
Condition and print('Yes(Triangle Possible)')
Condition or print('No(Triangle not Possible)')
