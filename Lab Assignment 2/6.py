# 6. Given two numbers ‘a’ and b’. Write a program to count number of bits needed to be flipped to convert ‘a’ to ‘b’.

a = int(input('Enter first number: '))
b = int(input('Enter second number: '))

# We can do this by calculating Xor of a and b, then converting the result to a binary form.
c = bin(a^b)

print("Number of bits that need to be flipped to convert 'a' to 'b' =", c.count('1'))
