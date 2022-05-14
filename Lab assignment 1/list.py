SID = int(input('Enter SID: '))
Name = str(input('Enter name: '))

Gender = str(input('Enter Gender(F, M, or U for Unknown): '))

# Gender constraints
while Gender not in ('F', 'M', 'U'):
    print('Invalid Gender Value, try again\n')
    Gender = str(input('Enter Gender(F, M or U for Unknown): '))

Course_Name = str(input('Enter Course_Name: '))
CGPA = float(input('Enter CGPA: '))

# CGPA constraints
while CGPA>10 or CGPA<0:
    print('Invalid CGPA Value, try again\n')
    CGPA = float(input('Enter CGPA: '))

Student = [SID,Name,Gender,Course_Name,CGPA]
print('Your data is:',Student)
