# 5. For any three lengths, there is a simple test to see if it is possible to form a triangle. If any of the three lengths is greater than the sum of the other two, then you cannot form a triangle.
# Otherwise, Enter three sides of a triangle, converts them to integers, and to check whether the given input lengths can form a triangle or not (Print : “Yes” or “No”).[Don’t use if else here].

# Inputting three sides of the triangle
a = int(input('Enter First side(in integers): '))
b = int(input('Enter Second side(in integers): '))
c = int(input('Enter Third side(in integers): '))

# Using Logical Operators as a Conditional Statement:
Condition = (a+b>c) and (b+c>a) and (a+c>b)
Condition and print('Yes(Triangle Possible)')
Condition or print('No(Triangle not Possible)')
