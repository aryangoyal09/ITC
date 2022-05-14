# 1. For a given input string “Python is a case sensitive language”. Write python code for the following:
# a. Find the length of the input string.
# b. Reverse the order of the string in one line code.
# c. Using Slice function store “a case sensitive” in new string.
# d. Replace “a case sensitive” with “object oriented”.
# e. Find index of substring “a” in the given input string.
# f. Remove the white spaces from the given input string.

line = 'Python is a case sensitive language'

# a.
print('Lenght of string is',len(line))
# b.
print(line[::-1])
# c.
new_line = line[12:26]
print(new_line)
# d.
print(line.replace('a case sensitive', 'an object oriented'))
# e.
print('Index of "a" in original string is', line.find('a'))
# f.
print(line.replace(' ', ''))
