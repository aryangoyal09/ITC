str = input("Enter string: ")
count = dict()

#Split the input string into words and store it in in a list
words = str.split(' ')

for i in words:
    if i in count:
        count[i] += 1
    else:
        count[i] = 1

print(count)
