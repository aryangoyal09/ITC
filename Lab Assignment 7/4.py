marks=[int(i) for i in input('Enter elements marks by space: ').split(' ')]

# Defining function
def partition(my_list, low, high):
    i=(low-1)
    pivot=my_list[high]
    for j in range(low, high):
        if my_list[j]<=pivot:
            i=i+1
            my_list[i], my_list[j]=my_list[j], my_list[i]
    my_list[i+1], my_list[high]=my_list[high], my_list[i+1]
    return (i+1)

# Quicksort function
def quick_sort(my_list, low, high):
    if len(my_list)==1:
        return my_list
    if low < high:
        pe=partition(my_list, low, high)
        quick_sort(my_list, low, pe-1)
        quick_sort(my_list, pe+1, high)

quick_sort(marks, 0, len(marks)-1)
print(marks)
