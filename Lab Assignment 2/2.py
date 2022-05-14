# 2. Store your name, SID, department name and CGPA into different variables.
# With the help of String formatting print the following output:
# Hey, ABC Here!
# My SID is 2110XXXX
# I am from XYZ department and my CGPA is 9.9

# Variables
Name = 'ABC'
SID = '2110xxxx'
Branch = 'XYZ'
CGPA = '9.9'

Intro = 'Hey, {} Here!\nMy SID is {}\nI am from {} Department and my CGPA is {}'

# String Formatting
print(Intro.format(Name,SID,Branch,CGPA))
