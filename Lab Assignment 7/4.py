list_size=int(input("Enter size of list: "))
marks=[] # list that will store marks
for i in range(0, list_size): # taking input of elements
    element=int(input("Enter marks: "))
    marks.append(element)

def partition(my_list, low, high): # function takes last element as pivot
    i=(low-1)
    pivot=my_list[high]
    for j in range(low, high): # sorts all elements smaller than pivot on its left and all elements greater on right side
        if my_list[j]<=pivot:
            i=i+1
            my_list[i], my_list[j]=my_list[j], my_list[i]
    my_list[i+1], my_list[high]=my_list[high], my_list[i+1]
    return (i+1)

def quick_sort(my_list, low, high): # function to do quick sort
    if len(my_list)==1:
        return my_list
    if low < high:
        pe=partition(my_list, low, high) # pe is partitioning element
        quick_sort(my_list, low, pe-1) # sorts elements before pe
        quick_sort(my_list, pe+1, high) # sorts elements after pe

quick_sort(marks, 0, list_size-1) # quick sort function is called for marks list
print(marks)
