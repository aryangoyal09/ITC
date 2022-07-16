array_size=int(input("Enter size of array: "))
array=[]
for i in range(0, array_size):
    element=int(input("Enter element "))
    array.append(element)

# PART-(a)
# Sorting the array
# Selection Sort Algorithm
for i in range(0, array_size):
    min_index=i
    for j in range(i+1, array_size):
        if array[min_index]>array[j]:
            min_index=j # finding minimum element
    array[i], array[min_index]=array[min_index], array[i] # swapping first element with minimum element
print(array)

x=int(input("Enter element to be searched and counted: "))

# PART-(b)
# Binary Search Algorithm
def binary_search(array, x):
    low=0
    high=len(array)-1
    mid=0
    while low<=high:
        mid=(high + low)//2
        if array[mid]<x: # if x is greater than mid element, ignore left half
            low=mid+1
        elif array[mid]>x: # if x is less than mid element, ignore right half
            high=mid-1
        else:
            return mid # this means x is present at mid position
    return -1 # in this case, x is not present

result=binary_search(array, x)
if result!=-1:
    print("Element is present at index", result)
else:
    print("Error! Element is not present.")

# PART-(c)
# Counting occurrences of element
def count(array, x): # function to count occurrences of element
    count=0
    for i in array:
        if i==x:
            count+=1
    return count

occurrences=count(array, x)
print("Number of occurrences of element is", occurrences)

#QUESTION 6
#REMOVING DUPLICATES AND SORTING

def selection_sort(array):  
    length = len(array)  
      
    for i in range(length-1):  
        minIndex = i  
          
        for j in range(i+1, length):  
            if array[j]<array[minIndex]:  
                minIndex = j  
                  
        array[i], array[minIndex] = array[minIndex], array[i]  
          
    return array
def bubbleSort(arr):
    n = len(arr)
    swapped = False
    for i in range(n-1):
        for j in range(0, n-i-1):
            if arr[j] > arr[j + 1]:
                swapped = True
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
        if not swapped:
            return
n=int(input("Enter number of inputs:"))
l=[]
for i in range(0,n):
    s=int(input("Enter number:"))
    l.append(s)
l=set(l)
l=list(l)
l.sort()
print(l)
