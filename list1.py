#Program to interchange first and last elements in a list

def swap(my_list):
    temp = my_list[0]
    my_list[0] = my_list[-1]
    my_list[-1] = temp
    return my_list

my_list = []
n = int(input('Enter the length of the list:'))
for i in range(0, n):
    el = input('Enter the {} element of the list:'.format(i))
    my_list.append(el)


print('After swapping')
print(swap(my_list))

#output
#Enter the length of the list:4
#Enter the 0 element of the list:1
#Enter the 1 element of the list:2
#Enter the 2 element of the list:3
#Enter the 3 element of the list:4
#After swapping
#['4', '2', '3', '1']