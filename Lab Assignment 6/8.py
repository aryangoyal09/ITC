# Making a class and defining the function sum_zero:
class answer:
    def sum_zero(self,list):
        output=[]
        for i in range(0, len(list)):
            for j in range(i+1, len(list)):
                for k in range(j+1, len(list)):
                    if list[i]+list[j]+list[k]==0:
                        output= output + [[list[i], list[j], list[k]]]
        if output==[]:
            print('No such triplets')
        else:
            print('The triplets that add up to zero are:', output)

input_list = [int(i) for i in input('Enter integers separated by space: ').split()]
answer().sum_zero(input_list)
