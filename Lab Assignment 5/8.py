# Input 10 integers
input_list = [int(i) for i in input('Enter 10 no. separated by space: ').split()]

# Checking if inputs are 10, otherwise telling user to enter again:
while len(input_list)!=10:
    input_list = [int(i) for i in input('Not 10 values, try again: ').split()]

# Sorting the list for an arranged output:
input_list.sort()

pos_nums=''
neg_nums=''
odd_nums=''
even_nums=''

for j in input_list:
    if j > 0 :
        pos_nums = pos_nums + ', ' + str(j)
    elif j < 0:
        neg_nums = neg_nums + ', ' + str(j)
for k in input_list:
    if k % 2 == 0:
        even_nums = even_nums + ', ' + str(k)
    else:
        odd_nums = odd_nums + ', ' + str(k)

# We are slicing the answer string because there's an additional ", " at the start
print('Positive numbers are:', pos_nums[2::])
print('Negative numbers are:', neg_nums[2::])
print('Odd numbers are:', odd_nums[2::])
print('Even numbers are:', even_nums[2::])

# To find number of times each number is entered:
for m in range(0,10):
    if m < 9:
        if input_list[m+1]==input_list[m]:
            continue
    count=0
    for n in range(0,10):
        if input_list[m]==input_list[n]:
            count+=1
    print('Count of', input_list[m], 'is', count)
