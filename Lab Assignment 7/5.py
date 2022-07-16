array=[int(i) for i in input('Enter elements marks by space: ').split(' ')]
for i in range(0, len(array)):
    element=int(input("Enter element "))
    array.append(element)

# Selection Sort Algorithm
for i in range(0, len(array)):
    min_index=i
    for j in range(i+1, len(array)):
        if array[min_index]>array[j]:
            min_index=j # finding minimum element
    array[i], array[min_index]=array[min_index], array[i] # swapping first element with minimum element
print(array)

x=int(input("Enter element to be searched and counted: "))

# Binary Search Algorithm
def binary_search(array, x):
    low=0
    high=len(array)-1
    mid=0
    while low<=high:
        mid=(high + low)//2
        if array[mid]<x:
            low=mid+1
        elif array[mid]>x:
            high=mid-1
        else:
            return mid
    return -1

result=binary_search(array, x)
if result!=-1:
    print("Element is present at index", result)
else:
    print("Error! Element is not present.")

# Function to count occurrences of element
def count(array, x): 
    count=0
    for i in array:
        if i==x:
            count+=1
    return count

occurrences=count(array, x)
print("Number of occurrences of element is", occurrences)
